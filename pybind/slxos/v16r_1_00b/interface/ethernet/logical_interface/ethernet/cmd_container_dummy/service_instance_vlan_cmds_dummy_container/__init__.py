
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import get_untagged_vlan_dummy
import tagged_outer_vlan
class service_instance_vlan_cmds_dummy_container(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/ethernet/logical-interface/ethernet/cmd-container-dummy/service-instance-vlan-cmds-dummy-container. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__get_untagged_vlan_dummy','__tagged_outer_vlan',)

  _yang_name = 'service-instance-vlan-cmds-dummy-container'
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
    self.__get_untagged_vlan_dummy = YANGDynClass(base=get_untagged_vlan_dummy.get_untagged_vlan_dummy, is_container='container', yang_name="get-untagged-vlan-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    self.__tagged_outer_vlan = YANGDynClass(base=tagged_outer_vlan.tagged_outer_vlan, is_container='container', yang_name="tagged-outer-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Outer VLAN for this logical interface', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)

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
      return [u'interface', u'ethernet', u'logical-interface', u'ethernet', u'cmd-container-dummy', u'service-instance-vlan-cmds-dummy-container']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'Ethernet', u'logical-interface', u'ethernet']

  def _get_get_untagged_vlan_dummy(self):
    """
    Getter method for get_untagged_vlan_dummy, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container/get_untagged_vlan_dummy (container)
    """
    return self.__get_untagged_vlan_dummy
      
  def _set_get_untagged_vlan_dummy(self, v, load=False):
    """
    Setter method for get_untagged_vlan_dummy, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container/get_untagged_vlan_dummy (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_get_untagged_vlan_dummy is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_get_untagged_vlan_dummy() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=get_untagged_vlan_dummy.get_untagged_vlan_dummy, is_container='container', yang_name="get-untagged-vlan-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """get_untagged_vlan_dummy must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=get_untagged_vlan_dummy.get_untagged_vlan_dummy, is_container='container', yang_name="get-untagged-vlan-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)""",
        })

    self.__get_untagged_vlan_dummy = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_get_untagged_vlan_dummy(self):
    self.__get_untagged_vlan_dummy = YANGDynClass(base=get_untagged_vlan_dummy.get_untagged_vlan_dummy, is_container='container', yang_name="get-untagged-vlan-dummy", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)


  def _get_tagged_outer_vlan(self):
    """
    Getter method for tagged_outer_vlan, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container/tagged_outer_vlan (container)
    """
    return self.__tagged_outer_vlan
      
  def _set_tagged_outer_vlan(self, v, load=False):
    """
    Setter method for tagged_outer_vlan, mapped from YANG variable /interface/ethernet/logical_interface/ethernet/cmd_container_dummy/service_instance_vlan_cmds_dummy_container/tagged_outer_vlan (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_tagged_outer_vlan is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_tagged_outer_vlan() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=tagged_outer_vlan.tagged_outer_vlan, is_container='container', yang_name="tagged-outer-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Outer VLAN for this logical interface', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """tagged_outer_vlan must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=tagged_outer_vlan.tagged_outer_vlan, is_container='container', yang_name="tagged-outer-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Outer VLAN for this logical interface', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)""",
        })

    self.__tagged_outer_vlan = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_tagged_outer_vlan(self):
    self.__tagged_outer_vlan = YANGDynClass(base=tagged_outer_vlan.tagged_outer_vlan, is_container='container', yang_name="tagged-outer-vlan", rest_name="vlan", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure Outer VLAN for this logical interface', u'cli-compact-syntax': None, u'cli-sequence-commands': None, u'alt-name': u'vlan'}}, namespace='urn:brocade.com:mgmt:brocade-lif', defining_module='brocade-lif', yang_type='container', is_config=True)

  get_untagged_vlan_dummy = __builtin__.property(_get_get_untagged_vlan_dummy, _set_get_untagged_vlan_dummy)
  tagged_outer_vlan = __builtin__.property(_get_tagged_outer_vlan, _set_tagged_outer_vlan)


  _pyangbind_elements = {'get_untagged_vlan_dummy': get_untagged_vlan_dummy, 'tagged_outer_vlan': tagged_outer_vlan, }


