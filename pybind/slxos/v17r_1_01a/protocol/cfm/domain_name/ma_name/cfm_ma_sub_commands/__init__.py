
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import mep
class cfm_ma_sub_commands(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/cfm/domain-name/ma-name/cfm-ma-sub-commands. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ccm_interval','__mip_policy','__maid_format','__mep',)

  _yang_name = 'cfm-ma-sub-commands'
  _rest_name = ''

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
    self.__ccm_interval = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'100-ms': {'value': 3}, u'10-seconds': {'value': 5}, u'1-second': {'value': 4}, u'3.3-ms': {'value': 1}, u'10-ms': {'value': 2}},), is_leaf=True, yang_name="ccm-interval", rest_name="ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'set CCM interval', u'cli-full-no': None, u'callpoint': u'setDot1agCcmInterval'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='ccm-interval-type', is_config=True)
    self.__maid_format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'long': {'value': 1}},), is_leaf=True, yang_name="maid-format", rest_name="maid-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MA ID Format to include domain details', u'cli-full-no': None, u'callpoint': u'setDot1agMaIdFormat'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='maid-format-type', is_config=True)
    self.__mip_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 1}, u'explicit': {'value': 2}},), is_leaf=True, yang_name="mip-policy", rest_name="mip-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MIP policy', u'cli-full-no': None, u'callpoint': u'setDot1agMipPolicy'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='mip-policy-type', is_config=True)
    self.__mep = YANGDynClass(base=YANGListType("mep_id",mep.mep, yang_name="mep", rest_name="mep", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mep-id', extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}), is_container='list', yang_name="mep", rest_name="mep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

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
      return [u'protocol', u'cfm', u'domain-name', u'ma-name', u'cfm-ma-sub-commands']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'cfm', u'domain-name', u'ma-name']

  def _get_ccm_interval(self):
    """
    Getter method for ccm_interval, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/ccm_interval (ccm-interval-type)
    """
    return self.__ccm_interval
      
  def _set_ccm_interval(self, v, load=False):
    """
    Setter method for ccm_interval, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/ccm_interval (ccm-interval-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ccm_interval is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ccm_interval() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'100-ms': {'value': 3}, u'10-seconds': {'value': 5}, u'1-second': {'value': 4}, u'3.3-ms': {'value': 1}, u'10-ms': {'value': 2}},), is_leaf=True, yang_name="ccm-interval", rest_name="ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'set CCM interval', u'cli-full-no': None, u'callpoint': u'setDot1agCcmInterval'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='ccm-interval-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ccm_interval must be of a type compatible with ccm-interval-type""",
          'defined-type': "brocade-dot1ag:ccm-interval-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'100-ms': {'value': 3}, u'10-seconds': {'value': 5}, u'1-second': {'value': 4}, u'3.3-ms': {'value': 1}, u'10-ms': {'value': 2}},), is_leaf=True, yang_name="ccm-interval", rest_name="ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'set CCM interval', u'cli-full-no': None, u'callpoint': u'setDot1agCcmInterval'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='ccm-interval-type', is_config=True)""",
        })

    self.__ccm_interval = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ccm_interval(self):
    self.__ccm_interval = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'100-ms': {'value': 3}, u'10-seconds': {'value': 5}, u'1-second': {'value': 4}, u'3.3-ms': {'value': 1}, u'10-ms': {'value': 2}},), is_leaf=True, yang_name="ccm-interval", rest_name="ccm-interval", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'set CCM interval', u'cli-full-no': None, u'callpoint': u'setDot1agCcmInterval'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='ccm-interval-type', is_config=True)


  def _get_mip_policy(self):
    """
    Getter method for mip_policy, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/mip_policy (mip-policy-type)
    """
    return self.__mip_policy
      
  def _set_mip_policy(self, v, load=False):
    """
    Setter method for mip_policy, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/mip_policy (mip-policy-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mip_policy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mip_policy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 1}, u'explicit': {'value': 2}},), is_leaf=True, yang_name="mip-policy", rest_name="mip-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MIP policy', u'cli-full-no': None, u'callpoint': u'setDot1agMipPolicy'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='mip-policy-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mip_policy must be of a type compatible with mip-policy-type""",
          'defined-type': "brocade-dot1ag:mip-policy-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 1}, u'explicit': {'value': 2}},), is_leaf=True, yang_name="mip-policy", rest_name="mip-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MIP policy', u'cli-full-no': None, u'callpoint': u'setDot1agMipPolicy'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='mip-policy-type', is_config=True)""",
        })

    self.__mip_policy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mip_policy(self):
    self.__mip_policy = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 1}, u'explicit': {'value': 2}},), is_leaf=True, yang_name="mip-policy", rest_name="mip-policy", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MIP policy', u'cli-full-no': None, u'callpoint': u'setDot1agMipPolicy'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='mip-policy-type', is_config=True)


  def _get_maid_format(self):
    """
    Getter method for maid_format, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/maid_format (maid-format-type)
    """
    return self.__maid_format
      
  def _set_maid_format(self, v, load=False):
    """
    Setter method for maid_format, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/maid_format (maid-format-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_maid_format is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_maid_format() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'long': {'value': 1}},), is_leaf=True, yang_name="maid-format", rest_name="maid-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MA ID Format to include domain details', u'cli-full-no': None, u'callpoint': u'setDot1agMaIdFormat'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='maid-format-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """maid_format must be of a type compatible with maid-format-type""",
          'defined-type': "brocade-dot1ag:maid-format-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'long': {'value': 1}},), is_leaf=True, yang_name="maid-format", rest_name="maid-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MA ID Format to include domain details', u'cli-full-no': None, u'callpoint': u'setDot1agMaIdFormat'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='maid-format-type', is_config=True)""",
        })

    self.__maid_format = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_maid_format(self):
    self.__maid_format = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'default': {'value': 0}, u'long': {'value': 1}},), is_leaf=True, yang_name="maid-format", rest_name="maid-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Set MA ID Format to include domain details', u'cli-full-no': None, u'callpoint': u'setDot1agMaIdFormat'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='maid-format-type', is_config=True)


  def _get_mep(self):
    """
    Getter method for mep, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/mep (list)
    """
    return self.__mep
      
  def _set_mep(self, v, load=False):
    """
    Setter method for mep, mapped from YANG variable /protocol/cfm/domain_name/ma_name/cfm_ma_sub_commands/mep (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mep is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mep() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("mep_id",mep.mep, yang_name="mep", rest_name="mep", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mep-id', extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}), is_container='list', yang_name="mep", rest_name="mep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mep must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("mep_id",mep.mep, yang_name="mep", rest_name="mep", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mep-id', extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}), is_container='list', yang_name="mep", rest_name="mep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)""",
        })

    self.__mep = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mep(self):
    self.__mep = YANGDynClass(base=YANGListType("mep_id",mep.mep, yang_name="mep", rest_name="mep", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='mep-id', extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}), is_container='list', yang_name="mep", rest_name="mep", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Maintanance EndPoint', u'cli-run-template-enter': u'$(.?:)', u'cli-full-no': None, u'cli-suppress-list-no': None, u'cli-sequence-commands': None, u'callpoint': u'setDot1agMep', u'cli-mode-name': u'config-cfm-md-ma-mep-$(mep-id)'}}, namespace='urn:brocade.com:mgmt:brocade-dot1ag', defining_module='brocade-dot1ag', yang_type='list', is_config=True)

  ccm_interval = __builtin__.property(_get_ccm_interval, _set_ccm_interval)
  mip_policy = __builtin__.property(_get_mip_policy, _set_mip_policy)
  maid_format = __builtin__.property(_get_maid_format, _set_maid_format)
  mep = __builtin__.property(_get_mep, _set_mep)


  _pyangbind_elements = {'ccm_interval': ccm_interval, 'mip_policy': mip_policy, 'maid_format': maid_format, 'mep': mep, }


