import random

from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Servico, Funcionario, Recursos
from .forms import ContatoForm
from django.contrib import messages

from django.utils.translation import gettext as _
from django.utils import translation


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        # Obtendo todos os recursos
        all_features = list(Recursos.objects.all())

        # Deiixando os recursos aleatórios e sem repetição
        random.shuffle(all_features)

        # Traduzindo os recursos antes de colocá-los no contexto
        for feature in all_features:
            feature.recurso = _(feature.recurso)
            feature.descricao = _(feature.descricao)

        # Trazendo os recursos no contexto
        context['features'] = all_features

        # Trazendo serviços e funcionário no contexto
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['lang'] = lang
        translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, _('E-mail enviado com sucesso'))
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, _('Erro ao enviar e-mail'))
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
