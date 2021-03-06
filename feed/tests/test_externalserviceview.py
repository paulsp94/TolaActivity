from django.test import TestCase
from rest_framework.test import APIRequestFactory

import factories
from feed.views import ExternalServiceViewSet
from workflow.models import WorkflowTeam, ROLE_ORGANIZATION_ADMIN, \
    ROLE_PROGRAM_TEAM, ROLE_PROGRAM_ADMIN, ROLE_VIEW_ONLY


class ExternalServiceListViewsTest(TestCase):
    def setUp(self):
        factories.Organization(id=1)
        factories.ExternalService.create_batch(2)
        self.factory = APIRequestFactory()
        self.tola_user = factories.TolaUser()

    def test_list_externalservice_superuser(self):
        request = self.factory.get('/api/externalservice/')
        request.user = factories.User.build(is_superuser=True,
                                            is_staff=True)
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_list_externalservice_org_admin(self):
        request = self.factory.get('/api/externalservice/')
        group_org_admin = factories.Group(name=ROLE_ORGANIZATION_ADMIN)
        self.tola_user.user.groups.add(group_org_admin)

        request.user = self.tola_user.user
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        factories.ExternalService(organization=self.tola_user.organization)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_externalservice_program_admin(self):
        request = self.factory.get('/api/externalservice/')
        WorkflowTeam.objects.create(
            workflow_user=self.tola_user,
            role=factories.Group(name=ROLE_PROGRAM_ADMIN))
        request.user = self.tola_user.user
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        factories.ExternalService(organization=self.tola_user.organization)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_externalservice_program_team(self):
        request = self.factory.get('/api/externalservice/')
        WorkflowTeam.objects.create(
            workflow_user=self.tola_user,
            role=factories.Group(name=ROLE_PROGRAM_TEAM))
        request.user = self.tola_user.user
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        factories.ExternalService(organization=self.tola_user.organization)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_list_externalservice_view_only(self):
        request = self.factory.get('/api/externalservice/')
        WorkflowTeam.objects.create(
            workflow_user=self.tola_user,
            role=factories.Group(name=ROLE_VIEW_ONLY))
        request.user = self.tola_user.user
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)

        factories.ExternalService(organization=self.tola_user.organization)
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)


class ExternalServiceFilterViewsTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.tola_user = factories.TolaUser()

    def test_filter_externalservice_superuser(self):
        self.tola_user.user.is_staff = True
        self.tola_user.user.is_superuser = True
        self.tola_user.user.save()

        ext_serv1 = factories.ExternalService(
            organization=self.tola_user.organization)
        factories.ExternalService(name='External Service B')
        request = self.factory.get('/api/externalservice/?organization__id=%s' %
                                   self.tola_user.organization.pk)
        request.user = self.tola_user.user
        view = ExternalServiceViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], ext_serv1.name)
