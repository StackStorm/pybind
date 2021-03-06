
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import rp_cand_interface
import rp_cand_grp_prefix
class rp_candidate(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-common-def - based on the path /routing-system/router/pim/rp-candidate. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__rp_cand_interface','__rp_cand_grp_prefix',)

  _yang_name = 'rp-candidate'
  _rest_name = 'rp-candidate'

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
    self.__rp_cand_grp_prefix = YANGDynClass(base=YANGListType("rp_cand_prefix_name",rp_cand_grp_prefix.rp_cand_grp_prefix, yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-prefix-name', extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}), is_container='list', yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)
    self.__rp_cand_interface = YANGDynClass(base=YANGListType("rp_cand_intf_type rp_cand_intf_id",rp_cand_interface.rp_cand_interface, yang_name="rp-cand-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-intf-type rp-cand-intf-id', extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}), is_container='list', yang_name="rp-cand-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)

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
      return [u'routing-system', u'router', u'pim', u'rp-candidate']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'pim', u'rp-candidate']

  def _get_rp_cand_interface(self):
    """
    Getter method for rp_cand_interface, mapped from YANG variable /routing_system/router/pim/rp_candidate/rp_cand_interface (list)
    """
    return self.__rp_cand_interface
      
  def _set_rp_cand_interface(self, v, load=False):
    """
    Setter method for rp_cand_interface, mapped from YANG variable /routing_system/router/pim/rp_candidate/rp_cand_interface (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_cand_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_cand_interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("rp_cand_intf_type rp_cand_intf_id",rp_cand_interface.rp_cand_interface, yang_name="rp-cand-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-intf-type rp-cand-intf-id', extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}), is_container='list', yang_name="rp-cand-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_cand_interface must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("rp_cand_intf_type rp_cand_intf_id",rp_cand_interface.rp_cand_interface, yang_name="rp-cand-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-intf-type rp-cand-intf-id', extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}), is_container='list', yang_name="rp-cand-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)""",
        })

    self.__rp_cand_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_cand_interface(self):
    self.__rp_cand_interface = YANGDynClass(base=YANGListType("rp_cand_intf_type rp_cand_intf_id",rp_cand_interface.rp_cand_interface, yang_name="rp-cand-interface", rest_name="interface", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-intf-type rp-cand-intf-id', extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}), is_container='list', yang_name="rp-cand-interface", rest_name="interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Interface information', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'interface', u'cli-compact-syntax': None, u'callpoint': u'PimCandRpCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)


  def _get_rp_cand_grp_prefix(self):
    """
    Getter method for rp_cand_grp_prefix, mapped from YANG variable /routing_system/router/pim/rp_candidate/rp_cand_grp_prefix (list)
    """
    return self.__rp_cand_grp_prefix
      
  def _set_rp_cand_grp_prefix(self, v, load=False):
    """
    Setter method for rp_cand_grp_prefix, mapped from YANG variable /routing_system/router/pim/rp_candidate/rp_cand_grp_prefix (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rp_cand_grp_prefix is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rp_cand_grp_prefix() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("rp_cand_prefix_name",rp_cand_grp_prefix.rp_cand_grp_prefix, yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-prefix-name', extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}), is_container='list', yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rp_cand_grp_prefix must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("rp_cand_prefix_name",rp_cand_grp_prefix.rp_cand_grp_prefix, yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-prefix-name', extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}), is_container='list', yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)""",
        })

    self.__rp_cand_grp_prefix = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rp_cand_grp_prefix(self):
    self.__rp_cand_grp_prefix = YANGDynClass(base=YANGListType("rp_cand_prefix_name",rp_cand_grp_prefix.rp_cand_grp_prefix, yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='rp-cand-prefix-name', extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}), is_container='list', yang_name="rp-cand-grp-prefix", rest_name="prefix", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'prefix list name', u'cli-suppress-mode': None, u'cli-suppress-list-no': None, u'alt-name': u'prefix', u'cli-compact-syntax': None, u'cli-suppress-key-abbreviation': None, u'callpoint': u'PimCandRpPrefixCfgCallpoint'}}, namespace='urn:brocade.com:mgmt:brocade-pim', defining_module='brocade-pim', yang_type='list', is_config=True)

  rp_cand_interface = __builtin__.property(_get_rp_cand_interface, _set_rp_cand_interface)
  rp_cand_grp_prefix = __builtin__.property(_get_rp_cand_grp_prefix, _set_rp_cand_grp_prefix)


  _pyangbind_elements = {'rp_cand_interface': rp_cand_interface, 'rp_cand_grp_prefix': rp_cand_grp_prefix, }


