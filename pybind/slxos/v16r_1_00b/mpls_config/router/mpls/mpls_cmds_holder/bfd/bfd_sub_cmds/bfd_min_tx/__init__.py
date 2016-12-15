
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class bfd_min_tx(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/bfd/bfd-sub-cmds/bfd-min-tx. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__bfd_min_tx_val','__bfd_min_rx','__bfd_multiplier',)

  _yang_name = 'bfd-min-tx'
  _rest_name = 'min-tx'

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
    self.__bfd_min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD Rx rate for control packets', u'alt-name': u'min-rx', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)
    self.__bfd_multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="bfd-multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of consecutive control packets to be missed for peer to be down', u'cli-full-no': None, u'alt-name': u'multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    self.__bfd_min_tx_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-tx-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'bfd', u'bfd-sub-cmds', u'bfd-min-tx']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'bfd', u'min-tx']

  def _get_bfd_min_tx_val(self):
    """
    Getter method for bfd_min_tx_val, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_min_tx_val (bfd-rate)
    """
    return self.__bfd_min_tx_val
      
  def _set_bfd_min_tx_val(self, v, load=False):
    """
    Setter method for bfd_min_tx_val, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_min_tx_val (bfd-rate)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_min_tx_val is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_min_tx_val() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-tx-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_min_tx_val must be of a type compatible with bfd-rate""",
          'defined-type': "brocade-mpls:bfd-rate",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-tx-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)""",
        })

    self.__bfd_min_tx_val = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_min_tx_val(self):
    self.__bfd_min_tx_val = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-tx-val", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)


  def _get_bfd_min_rx(self):
    """
    Getter method for bfd_min_rx, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_min_rx (bfd-rate)
    """
    return self.__bfd_min_rx
      
  def _set_bfd_min_rx(self, v, load=False):
    """
    Setter method for bfd_min_rx, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_min_rx (bfd-rate)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_min_rx is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_min_rx() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD Rx rate for control packets', u'alt-name': u'min-rx', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_min_rx must be of a type compatible with bfd-rate""",
          'defined-type': "brocade-mpls:bfd-rate",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD Rx rate for control packets', u'alt-name': u'min-rx', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)""",
        })

    self.__bfd_min_rx = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_min_rx(self):
    self.__bfd_min_rx = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'50..30000']}), is_leaf=True, yang_name="bfd-min-rx", rest_name="min-rx", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'BFD Rx rate for control packets', u'alt-name': u'min-rx', u'cli-incomplete-no': None, u'cli-incomplete-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='bfd-rate', is_config=True)


  def _get_bfd_multiplier(self):
    """
    Getter method for bfd_multiplier, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_multiplier (uint32)
    """
    return self.__bfd_multiplier
      
  def _set_bfd_multiplier(self, v, load=False):
    """
    Setter method for bfd_multiplier, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/bfd/bfd_sub_cmds/bfd_min_tx/bfd_multiplier (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bfd_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bfd_multiplier() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="bfd-multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of consecutive control packets to be missed for peer to be down', u'cli-full-no': None, u'alt-name': u'multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bfd_multiplier must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="bfd-multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of consecutive control packets to be missed for peer to be down', u'cli-full-no': None, u'alt-name': u'multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)""",
        })

    self.__bfd_multiplier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bfd_multiplier(self):
    self.__bfd_multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'3..50']}), is_leaf=True, yang_name="bfd-multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Number of consecutive control packets to be missed for peer to be down', u'cli-full-no': None, u'alt-name': u'multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='uint32', is_config=True)

  bfd_min_tx_val = __builtin__.property(_get_bfd_min_tx_val, _set_bfd_min_tx_val)
  bfd_min_rx = __builtin__.property(_get_bfd_min_rx, _set_bfd_min_rx)
  bfd_multiplier = __builtin__.property(_get_bfd_multiplier, _set_bfd_multiplier)


  _pyangbind_elements = {'bfd_min_tx_val': bfd_min_tx_val, 'bfd_min_rx': bfd_min_rx, 'bfd_multiplier': bfd_multiplier, }


