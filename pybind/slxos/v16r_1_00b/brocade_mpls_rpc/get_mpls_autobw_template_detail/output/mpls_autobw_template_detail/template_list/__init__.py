
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import associated_paths
class template_list(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /brocade_mpls_rpc/get-mpls-autobw-template-detail/output/mpls-autobw-template-detail/template-list. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__autobwTemplateName','__adjustmentInterval','__adjustmentThreshold','__overflowLimit','__underflowLimit','__mode','__associated_paths',)

  _yang_name = 'template-list'
  _rest_name = 'template-list'

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
    self.__underflowLimit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="underflowLimit", rest_name="underflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__adjustmentThreshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentThreshold", rest_name="adjustmentThreshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__associated_paths = YANGDynClass(base=YANGListType("lspName pathName",associated_paths.associated_paths, yang_name="associated-paths", rest_name="associated-paths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lspName pathName', extensions=None), is_container='list', yang_name="associated-paths", rest_name="associated-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    self.__autobwTemplateName = YANGDynClass(base=unicode, is_leaf=True, yang_name="autobwTemplateName", rest_name="autobwTemplateName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__overflowLimit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="overflowLimit", rest_name="overflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__adjustmentInterval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentInterval", rest_name="adjustmentInterval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

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
      return [u'brocade_mpls_rpc', u'get-mpls-autobw-template-detail', u'output', u'mpls-autobw-template-detail', u'template-list']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-mpls-autobw-template-detail', u'output', u'mpls-autobw-template-detail', u'template-list']

  def _get_autobwTemplateName(self):
    """
    Getter method for autobwTemplateName, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/autobwTemplateName (string)

    YANG Description: Name
    """
    return self.__autobwTemplateName
      
  def _set_autobwTemplateName(self, v, load=False):
    """
    Setter method for autobwTemplateName, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/autobwTemplateName (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_autobwTemplateName is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_autobwTemplateName() directly.

    YANG Description: Name
    """
    parent = getattr(self, "_parent", None)
    if parent is not None and load is False:
      raise AttributeError("Cannot set keys directly when" +
                             " within an instantiated list")

    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="autobwTemplateName", rest_name="autobwTemplateName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """autobwTemplateName must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="autobwTemplateName", rest_name="autobwTemplateName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)""",
        })

    self.__autobwTemplateName = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_autobwTemplateName(self):
    self.__autobwTemplateName = YANGDynClass(base=unicode, is_leaf=True, yang_name="autobwTemplateName", rest_name="autobwTemplateName", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, is_keyval=True, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='string', is_config=True)


  def _get_adjustmentInterval(self):
    """
    Getter method for adjustmentInterval, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/adjustmentInterval (uint32)

    YANG Description: Interval
    """
    return self.__adjustmentInterval
      
  def _set_adjustmentInterval(self, v, load=False):
    """
    Setter method for adjustmentInterval, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/adjustmentInterval (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjustmentInterval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjustmentInterval() directly.

    YANG Description: Interval
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentInterval", rest_name="adjustmentInterval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjustmentInterval must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentInterval", rest_name="adjustmentInterval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__adjustmentInterval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjustmentInterval(self):
    self.__adjustmentInterval = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentInterval", rest_name="adjustmentInterval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_adjustmentThreshold(self):
    """
    Getter method for adjustmentThreshold, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/adjustmentThreshold (uint32)

    YANG Description: Threshold
    """
    return self.__adjustmentThreshold
      
  def _set_adjustmentThreshold(self, v, load=False):
    """
    Setter method for adjustmentThreshold, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/adjustmentThreshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_adjustmentThreshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_adjustmentThreshold() directly.

    YANG Description: Threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentThreshold", rest_name="adjustmentThreshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """adjustmentThreshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentThreshold", rest_name="adjustmentThreshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__adjustmentThreshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_adjustmentThreshold(self):
    self.__adjustmentThreshold = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="adjustmentThreshold", rest_name="adjustmentThreshold", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_overflowLimit(self):
    """
    Getter method for overflowLimit, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/overflowLimit (uint32)

    YANG Description: Overflow Limit
    """
    return self.__overflowLimit
      
  def _set_overflowLimit(self, v, load=False):
    """
    Setter method for overflowLimit, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/overflowLimit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_overflowLimit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_overflowLimit() directly.

    YANG Description: Overflow Limit
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="overflowLimit", rest_name="overflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """overflowLimit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="overflowLimit", rest_name="overflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__overflowLimit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_overflowLimit(self):
    self.__overflowLimit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="overflowLimit", rest_name="overflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_underflowLimit(self):
    """
    Getter method for underflowLimit, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/underflowLimit (uint32)

    YANG Description: Underflow Limit
    """
    return self.__underflowLimit
      
  def _set_underflowLimit(self, v, load=False):
    """
    Setter method for underflowLimit, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/underflowLimit (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_underflowLimit is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_underflowLimit() directly.

    YANG Description: Underflow Limit
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="underflowLimit", rest_name="underflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """underflowLimit must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="underflowLimit", rest_name="underflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__underflowLimit = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_underflowLimit(self):
    self.__underflowLimit = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="underflowLimit", rest_name="underflowLimit", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/mode (uint32)

    YANG Description: Mode
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/mode (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.

    YANG Description: Mode
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)


  def _get_associated_paths(self):
    """
    Getter method for associated_paths, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/associated_paths (list)
    """
    return self.__associated_paths
      
  def _set_associated_paths(self, v, load=False):
    """
    Setter method for associated_paths, mapped from YANG variable /brocade_mpls_rpc/get_mpls_autobw_template_detail/output/mpls_autobw_template_detail/template_list/associated_paths (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_associated_paths is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_associated_paths() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("lspName pathName",associated_paths.associated_paths, yang_name="associated-paths", rest_name="associated-paths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lspName pathName', extensions=None), is_container='list', yang_name="associated-paths", rest_name="associated-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """associated_paths must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("lspName pathName",associated_paths.associated_paths, yang_name="associated-paths", rest_name="associated-paths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lspName pathName', extensions=None), is_container='list', yang_name="associated-paths", rest_name="associated-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)""",
        })

    self.__associated_paths = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_associated_paths(self):
    self.__associated_paths = YANGDynClass(base=YANGListType("lspName pathName",associated_paths.associated_paths, yang_name="associated-paths", rest_name="associated-paths", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='lspName pathName', extensions=None), is_container='list', yang_name="associated-paths", rest_name="associated-paths", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='list', is_config=True)

  autobwTemplateName = __builtin__.property(_get_autobwTemplateName, _set_autobwTemplateName)
  adjustmentInterval = __builtin__.property(_get_adjustmentInterval, _set_adjustmentInterval)
  adjustmentThreshold = __builtin__.property(_get_adjustmentThreshold, _set_adjustmentThreshold)
  overflowLimit = __builtin__.property(_get_overflowLimit, _set_overflowLimit)
  underflowLimit = __builtin__.property(_get_underflowLimit, _set_underflowLimit)
  mode = __builtin__.property(_get_mode, _set_mode)
  associated_paths = __builtin__.property(_get_associated_paths, _set_associated_paths)


  _pyangbind_elements = {'autobwTemplateName': autobwTemplateName, 'adjustmentInterval': adjustmentInterval, 'adjustmentThreshold': adjustmentThreshold, 'overflowLimit': overflowLimit, 'underflowLimit': underflowLimit, 'mode': mode, 'associated_paths': associated_paths, }


