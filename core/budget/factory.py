import factory

from core.budget.models import Budget, BudgetGroup, BudgetToGroupRelation


class BudgetGroupFactory(factory.django.DjangoModelFactory):
    mame = factory.Faker("first_name")

    class Meta:
        model = BudgetGroup


class BudgetFactory(factory.django.DjangoModelFactory):
    mame = factory.Faker("first_name")

    class Meta:
        model = Budget


class BudgetToGroupRelationFactory(factory.django.DjangoModelFactory):
    group = factory.SubFactory(BudgetGroupFactory)
    budget = factory.SubFactory(BudgetGroupFactory)

    class Meta:
        model = BudgetToGroupRelation


class BudgetWithGroupFactory(BudgetFactory):
    groups = factory.RelatedFactory(BudgetToGroupRelationFactory, factory_related_name='budget', )
