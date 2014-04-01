# -*- coding: utf-8 -*-
# vim: set expandtab tabstop=4 shiftwidth=4:
###############################################################
#                                                             #
#  Alexandre Defendi   -   01/04/2014                         #
#                                                             #
#  Módulo Básico - PyCrackCaptcha                             #
#                                                             #
#                                                             #
#                                                             #
#                                                             #
#                                                             #
###############################################################

class CCaptchaData(object):
    """ Interface para Implementações de Cracks """

    def __init__(self, **kwargs):
        self._arquivo = kwargs.pop('arquivo', False)

    def _get_arquivo(self):
        if self._arquivo is not None:
            return "%s" % self._arquivo
        else:
            return False

    def _set_arquivo(self, val):
        if val:
            self._arquivo = val
        else:
            self._arquivo = False

    arquivo = property(_get_arquivo, _set_arquivo)