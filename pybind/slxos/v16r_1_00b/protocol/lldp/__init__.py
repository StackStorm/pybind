
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import advertise
import profile
class lldp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol/lldp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__description','__hello','__mode','__multiplier','__advertise','__system_name','__system_description','__iscsi_priority','__disable','__profile',)

  _yang_name = 'lldp'
  _rest_name = 'lldp'

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
    self.__system_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([a-zA-Z]{1}([-a-zA-Z0-9\\s\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31}))|(\\s)*)', 'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="system-name", rest_name="system-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Name'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    self.__iscsi_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 50']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The User description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    self.__system_description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..50']}), is_leaf=True, yang_name="system-description", rest_name="system-description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Description.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    self.__disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    self.__profile = YANGDynClass(base=YANGListType("profile_name",profile.profile, yang_name="profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-name', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}), is_container='list', yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='list', is_config=True)
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The LLDP mode.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Timeout Multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    self.__advertise = YANGDynClass(base=advertise.advertise, is_container='container', presence=False, yang_name="advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Advertise TLV configuration.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    self.__hello = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..180']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Hello Transmit interval.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)

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
      return [u'protocol', u'lldp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol', u'lldp']

  def _get_description(self):
    """
    Getter method for description, mapped from YANG variable /protocol/lldp/description (string)
    """
    return self.__description
      
  def _set_description(self, v, load=False):
    """
    Setter method for description, mapped from YANG variable /protocol/lldp/description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_description() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 50']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The User description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 50']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The User description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)""",
        })

    self.__description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_description(self):
    self.__description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1 .. 50']}), is_leaf=True, yang_name="description", rest_name="description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The User description', u'cli-multi-value': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)


  def _get_hello(self):
    """
    Getter method for hello, mapped from YANG variable /protocol/lldp/hello (uint32)
    """
    return self.__hello
      
  def _set_hello(self, v, load=False):
    """
    Setter method for hello, mapped from YANG variable /protocol/lldp/hello (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_hello is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_hello() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..180']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Hello Transmit interval.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """hello must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..180']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Hello Transmit interval.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)""",
        })

    self.__hello = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_hello(self):
    self.__hello = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'4..180']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(30), is_leaf=True, yang_name="hello", rest_name="hello", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Hello Transmit interval.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)


  def _get_mode(self):
    """
    Getter method for mode, mapped from YANG variable /protocol/lldp/mode (enumeration)
    """
    return self.__mode
      
  def _set_mode(self, v, load=False):
    """
    Setter method for mode, mapped from YANG variable /protocol/lldp/mode (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mode is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mode() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The LLDP mode.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mode must be of a type compatible with enumeration""",
          'defined-type': "brocade-lldp:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The LLDP mode.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)""",
        })

    self.__mode = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mode(self):
    self.__mode = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'rx': {'value': 2}, u'tx': {'value': 1}},), is_leaf=True, yang_name="mode", rest_name="mode", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The LLDP mode.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='enumeration', is_config=True)


  def _get_multiplier(self):
    """
    Getter method for multiplier, mapped from YANG variable /protocol/lldp/multiplier (uint32)
    """
    return self.__multiplier
      
  def _set_multiplier(self, v, load=False):
    """
    Setter method for multiplier, mapped from YANG variable /protocol/lldp/multiplier (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_multiplier is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_multiplier() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Timeout Multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """multiplier must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Timeout Multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)""",
        })

    self.__multiplier = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_multiplier(self):
    self.__multiplier = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'2..10']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="multiplier", rest_name="multiplier", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Timeout Multiplier'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)


  def _get_advertise(self):
    """
    Getter method for advertise, mapped from YANG variable /protocol/lldp/advertise (container)
    """
    return self.__advertise
      
  def _set_advertise(self, v, load=False):
    """
    Setter method for advertise, mapped from YANG variable /protocol/lldp/advertise (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_advertise is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_advertise() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=advertise.advertise, is_container='container', presence=False, yang_name="advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Advertise TLV configuration.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """advertise must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=advertise.advertise, is_container='container', presence=False, yang_name="advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Advertise TLV configuration.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)""",
        })

    self.__advertise = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_advertise(self):
    self.__advertise = YANGDynClass(base=advertise.advertise, is_container='container', presence=False, yang_name="advertise", rest_name="advertise", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'The Advertise TLV configuration.', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)


  def _get_system_name(self):
    """
    Getter method for system_name, mapped from YANG variable /protocol/lldp/system_name (string)
    """
    return self.__system_name
      
  def _set_system_name(self, v, load=False):
    """
    Setter method for system_name, mapped from YANG variable /protocol/lldp/system_name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_name() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([a-zA-Z]{1}([-a-zA-Z0-9\\s\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31}))|(\\s)*)', 'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="system-name", rest_name="system-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Name'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([a-zA-Z]{1}([-a-zA-Z0-9\\s\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31}))|(\\s)*)', 'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="system-name", rest_name="system-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Name'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)""",
        })

    self.__system_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_name(self):
    self.__system_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'(([a-zA-Z]{1}([-a-zA-Z0-9\\s\\.\\\\\\\\@#\\+\\*\\(\\)=\\{~\\}%<>=$_\\[\\]\\|]{0,31}))|(\\s)*)', 'length': [u'0..32']}), default=unicode(""), is_leaf=True, yang_name="system-name", rest_name="system-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Name'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)


  def _get_system_description(self):
    """
    Getter method for system_description, mapped from YANG variable /protocol/lldp/system_description (string)
    """
    return self.__system_description
      
  def _set_system_description(self, v, load=False):
    """
    Setter method for system_description, mapped from YANG variable /protocol/lldp/system_description (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_system_description is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_system_description() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..50']}), is_leaf=True, yang_name="system-description", rest_name="system-description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Description.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """system_description must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..50']}), is_leaf=True, yang_name="system-description", rest_name="system-description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Description.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)""",
        })

    self.__system_description = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_system_description(self):
    self.__system_description = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'length': [u'1..50']}), is_leaf=True, yang_name="system-description", rest_name="system-description", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-multi-value': None, u'info': u'The System Description.'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='string', is_config=True)


  def _get_iscsi_priority(self):
    """
    Getter method for iscsi_priority, mapped from YANG variable /protocol/lldp/iscsi_priority (uint32)
    """
    return self.__iscsi_priority
      
  def _set_iscsi_priority(self, v, load=False):
    """
    Setter method for iscsi_priority, mapped from YANG variable /protocol/lldp/iscsi_priority (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_iscsi_priority is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_iscsi_priority() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """iscsi_priority must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)""",
        })

    self.__iscsi_priority = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_iscsi_priority(self):
    self.__iscsi_priority = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0..7']}), default=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32)(4), is_leaf=True, yang_name="iscsi-priority", rest_name="iscsi-priority", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Configure the Ethernet priority to advertise for iSCSI', u'hidden': u'full'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='uint32', is_config=True)


  def _get_disable(self):
    """
    Getter method for disable, mapped from YANG variable /protocol/lldp/disable (empty)
    """
    return self.__disable
      
  def _set_disable(self, v, load=False):
    """
    Setter method for disable, mapped from YANG variable /protocol/lldp/disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)""",
        })

    self.__disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_disable(self):
    self.__disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Disable LLDP'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='empty', is_config=True)


  def _get_profile(self):
    """
    Getter method for profile, mapped from YANG variable /protocol/lldp/profile (list)
    """
    return self.__profile
      
  def _set_profile(self, v, load=False):
    """
    Setter method for profile, mapped from YANG variable /protocol/lldp/profile (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_profile is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_profile() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("profile_name",profile.profile, yang_name="profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-name', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}), is_container='list', yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """profile must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("profile_name",profile.profile, yang_name="profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-name', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}), is_container='list', yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='list', is_config=True)""",
        })

    self.__profile = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_profile(self):
    self.__profile = YANGDynClass(base=YANGListType("profile_name",profile.profile, yang_name="profile", rest_name="profile", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='profile-name', extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}), is_container='list', yang_name="profile", rest_name="profile", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'The LLDP Profile table.', u'callpoint': u'lldp_global_profile_conf'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='list', is_config=True)

  description = __builtin__.property(_get_description, _set_description)
  hello = __builtin__.property(_get_hello, _set_hello)
  mode = __builtin__.property(_get_mode, _set_mode)
  multiplier = __builtin__.property(_get_multiplier, _set_multiplier)
  advertise = __builtin__.property(_get_advertise, _set_advertise)
  system_name = __builtin__.property(_get_system_name, _set_system_name)
  system_description = __builtin__.property(_get_system_description, _set_system_description)
  iscsi_priority = __builtin__.property(_get_iscsi_priority, _set_iscsi_priority)
  disable = __builtin__.property(_get_disable, _set_disable)
  profile = __builtin__.property(_get_profile, _set_profile)


  _pyangbind_elements = {'description': description, 'hello': hello, 'mode': mode, 'multiplier': multiplier, 'advertise': advertise, 'system_name': system_name, 'system_description': system_description, 'iscsi_priority': iscsi_priority, 'disable': disable, 'profile': profile, }


