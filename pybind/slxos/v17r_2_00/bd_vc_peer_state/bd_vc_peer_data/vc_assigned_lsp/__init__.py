
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class vc_assigned_lsp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-pwm-operational - based on the path /bd-vc-peer-state/bd-vc-peer-data/vc-assigned-lsp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description:  VC assigned lsp
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__vc_lsp_name',)

  _yang_name = 'vc-assigned-lsp'
  _rest_name = 'vc-assigned-lsp'

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
    self.__vc_lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", rest_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)

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
      return [u'bd-vc-peer-state', u'bd-vc-peer-data', u'vc-assigned-lsp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'bd-vc-peer-state', u'bd-vc-peer-data', u'vc-assigned-lsp']

  def _get_vc_lsp_name(self):
    """
    Getter method for vc_lsp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_assigned_lsp/vc_lsp_name (string)

    YANG Description: lsp name
    """
    return self.__vc_lsp_name
      
  def _set_vc_lsp_name(self, v, load=False):
    """
    Setter method for vc_lsp_name, mapped from YANG variable /bd_vc_peer_state/bd_vc_peer_data/vc_assigned_lsp/vc_lsp_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_vc_lsp_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_vc_lsp_name() directly.

    YANG Description: lsp name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="vc-lsp-name", rest_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """vc_lsp_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", rest_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)""",
        })

    self.__vc_lsp_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_vc_lsp_name(self):
    self.__vc_lsp_name = YANGDynClass(base=unicode, is_leaf=True, yang_name="vc-lsp-name", rest_name="vc-lsp-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-pwm-operational', defining_module='brocade-pwm-operational', yang_type='string', is_config=False)

  vc_lsp_name = __builtin__.property(_get_vc_lsp_name)


  _pyangbind_elements = {'vc_lsp_name': vc_lsp_name, }


