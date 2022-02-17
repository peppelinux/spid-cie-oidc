from django.test import TestCase, Client
from django.urls import reverse

from spid_cie_oidc.entity.jwtse import verify_jws
from spid_cie_oidc.entity.models import *
from spid_cie_oidc.entity.trust_chain import trust_chain_builder
from spid_cie_oidc.onboarding.models import *

from spid_cie_oidc.entity.tests.settings import *
from spid_cie_oidc.onboarding.tests.settings import *


class OnBoardingTest(TestCase):

    def setUp(self):
        self.ta_conf = FederationEntityConfiguration.objects.create(**ta_conf_data)
        self.rp_profile = FederationEntityProfile.objects.create(**RP_PROFILE)

        self.rp = FederationDescendant.objects.create(**rp_onboarding_data)
        self.rp_jwk = PublicJwk.objects.create()

        FederationDescendantJwk.objects.create(
            descendant=self.rp,
            jwk = self.rp_jwk
        )
        FederationEntityAssignedProfile.objects.create(
            descendant = self.rp,
            profile = self.rp_profile,
            issuer = self.ta_conf
        )

    def test_fetch_endpoint(self):
        url = reverse('oidcfed_fetch')
        c = Client()
        res = c.get(url, data={'sub': self.rp.sub})
        verify_jws(res.content.decode(), self.ta_conf.jwks[0])

    def test_list_endpoint(self):
        url = reverse('oidcfed_list')
        c = Client()
        res = c.get(url, data={'is_leaf': True})
        self.assertTrue(
            res.json()[0] == self.rp.sub
        )
        res = c.get(url, data={'is_leaf': False})
        self.assertFalse(res.json())

    # def test_trust_chain(self):
        # trust_chain_builder(
            # subject = rp_onboarding_data['sub'],
            
        # )