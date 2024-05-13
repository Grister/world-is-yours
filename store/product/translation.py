from modeltranslation.translator import translator, TranslationOptions
from .models import ProductSubCategory, ProductCategory, Product, ProductSpecs


class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'material', 'care', 'features')


class ProductSpecsTranslationOptions(TranslationOptions):
    fields = ('name', 'value')


translator.register(ProductSubCategory, ProductCategoryTranslationOptions)
translator.register(ProductCategory, ProductCategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ProductSpecs, ProductSpecsTranslationOptions)
