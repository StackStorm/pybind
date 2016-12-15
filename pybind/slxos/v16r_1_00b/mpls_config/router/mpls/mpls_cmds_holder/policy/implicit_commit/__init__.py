
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class implicit_commit(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/policy/implicit-commit. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__implicit_commit_all','__implicit_commit_autobw_adjustment','__implicit_commit_lsp_reoptimize_timer',)

  _yang_name = 'implicit-commit'
  _rest_name = 'implicit-commit'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    path_helper_ = kwargs.pop("path_helper", None)
    if path_helper_ is False:
      self._path_helper = False
    elif path_helper_ is not None and isinstance(path_helper_, xpathhelper.YANGPathHelper):
      self._path_helper = path_helper_
    elif hasattr(self, "_parent"):
      path_helper_ = getattr(self._parent, "_path_helper", False)
      self._path_helper = path_helper_
    else:
      self._path_helper = False

    extmethods = kwargs.pop("extmethods", None)
    if extmethods is False:
      self._extmethods = False
    elif extmethods is not None and isinstance(extmethods, dict):
      self._extmethods = extmethods
    elif hasattr(self, "_parent"):
      extmethods = getattr(self._parent, "_extmethods", None)
      self._extmethods = extmethods
    else:
      self._extmethods = False
    self.__implicit_commit_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-all", rest_name="all", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for all triggers', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__implicit_commit_autobw_adjustment = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-autobw-adjustment", rest_name="auto-bandwidth-adjustment", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for auto-bandwidth adjustments', u'hidden': u'full', u'alt-name': u'auto-bandwidth-adjustment'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__implicit_commit_lsp_reoptimize_timer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-lsp-reoptimize-timer", rest_name="lsp-reoptimize-timer", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for reoptimizations', u'alt-name': u'lsp-reoptimize-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'policy', u'implicit-commit']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'policy', u'implicit-commit']

  def _get_implicit_commit_all(self):
    """
    Getter method for implicit_commit_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_all (empty)
    """
    return self.__implicit_commit_all
      
  def _set_implicit_commit_all(self, v, load=False):
    """
    Setter method for implicit_commit_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_implicit_commit_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_implicit_commit_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="implicit-commit-all", rest_name="all", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for all triggers', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """implicit_commit_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-all", rest_name="all", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for all triggers', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__implicit_commit_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_implicit_commit_all(self):
    self.__implicit_commit_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-all", rest_name="all", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-all'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for all triggers', u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_implicit_commit_autobw_adjustment(self):
    """
    Getter method for implicit_commit_autobw_adjustment, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_autobw_adjustment (empty)
    """
    return self.__implicit_commit_autobw_adjustment
      
  def _set_implicit_commit_autobw_adjustment(self, v, load=False):
    """
    Setter method for implicit_commit_autobw_adjustment, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_autobw_adjustment (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_implicit_commit_autobw_adjustment is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_implicit_commit_autobw_adjustment() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="implicit-commit-autobw-adjustment", rest_name="auto-bandwidth-adjustment", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for auto-bandwidth adjustments', u'hidden': u'full', u'alt-name': u'auto-bandwidth-adjustment'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """implicit_commit_autobw_adjustment must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-autobw-adjustment", rest_name="auto-bandwidth-adjustment", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for auto-bandwidth adjustments', u'hidden': u'full', u'alt-name': u'auto-bandwidth-adjustment'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__implicit_commit_autobw_adjustment = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_implicit_commit_autobw_adjustment(self):
    self.__implicit_commit_autobw_adjustment = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-autobw-adjustment", rest_name="auto-bandwidth-adjustment", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for auto-bandwidth adjustments', u'hidden': u'full', u'alt-name': u'auto-bandwidth-adjustment'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_implicit_commit_lsp_reoptimize_timer(self):
    """
    Getter method for implicit_commit_lsp_reoptimize_timer, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_lsp_reoptimize_timer (empty)
    """
    return self.__implicit_commit_lsp_reoptimize_timer
      
  def _set_implicit_commit_lsp_reoptimize_timer(self, v, load=False):
    """
    Setter method for implicit_commit_lsp_reoptimize_timer, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/policy/implicit_commit/implicit_commit_lsp_reoptimize_timer (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_implicit_commit_lsp_reoptimize_timer is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_implicit_commit_lsp_reoptimize_timer() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="implicit-commit-lsp-reoptimize-timer", rest_name="lsp-reoptimize-timer", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for reoptimizations', u'alt-name': u'lsp-reoptimize-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """implicit_commit_lsp_reoptimize_timer must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-lsp-reoptimize-timer", rest_name="lsp-reoptimize-timer", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for reoptimizations', u'alt-name': u'lsp-reoptimize-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__implicit_commit_lsp_reoptimize_timer = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_implicit_commit_lsp_reoptimize_timer(self):
    self.__implicit_commit_lsp_reoptimize_timer = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="implicit-commit-lsp-reoptimize-timer", rest_name="lsp-reoptimize-timer", parent=self, choice=(u'implicit-commit-options', u'implicit-commit-case-selective'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Enable implicit commit for reoptimizations', u'alt-name': u'lsp-reoptimize-timer'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  implicit_commit_all = __builtin__.property(_get_implicit_commit_all, _set_implicit_commit_all)
  implicit_commit_autobw_adjustment = __builtin__.property(_get_implicit_commit_autobw_adjustment, _set_implicit_commit_autobw_adjustment)
  implicit_commit_lsp_reoptimize_timer = __builtin__.property(_get_implicit_commit_lsp_reoptimize_timer, _set_implicit_commit_lsp_reoptimize_timer)

  __choices__ = {u'implicit-commit-options': {u'implicit-commit-case-all': [u'implicit_commit_all'], u'implicit-commit-case-selective': [u'implicit_commit_autobw_adjustment', u'implicit_commit_lsp_reoptimize_timer']}}
  _pyangbind_elements = {'implicit_commit_all': implicit_commit_all, 'implicit_commit_autobw_adjustment': implicit_commit_autobw_adjustment, 'implicit_commit_lsp_reoptimize_timer': implicit_commit_lsp_reoptimize_timer, }


