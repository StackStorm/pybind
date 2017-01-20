
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import ospf_interface_config
class interface_loopback_ospf_conf(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/interface/loopback/ip/interface-loopback-ospf-conf. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ospf_interface_config',)

  _yang_name = 'interface-loopback-ospf-conf'
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
    self.__ospf_interface_config = YANGDynClass(base=ospf_interface_config.ospf_interface_config, is_container='container', presence=False, yang_name="ospf-interface-config", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF).', u'cli-incomplete-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'sort-priority': u'113', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'interface', u'loopback', u'ip', u'interface-loopback-ospf-conf']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'interface', u'Loopback', u'ip']

  def _get_ospf_interface_config(self):
    """
    Getter method for ospf_interface_config, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config (container)
    """
    return self.__ospf_interface_config
      
  def _set_ospf_interface_config(self, v, load=False):
    """
    Setter method for ospf_interface_config, mapped from YANG variable /rbridge_id/interface/loopback/ip/interface_loopback_ospf_conf/ospf_interface_config (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ospf_interface_config is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ospf_interface_config() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=ospf_interface_config.ospf_interface_config, is_container='container', presence=False, yang_name="ospf-interface-config", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF).', u'cli-incomplete-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'sort-priority': u'113', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ospf_interface_config must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=ospf_interface_config.ospf_interface_config, is_container='container', presence=False, yang_name="ospf-interface-config", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF).', u'cli-incomplete-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'sort-priority': u'113', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)""",
        })

    self.__ospf_interface_config = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ospf_interface_config(self):
    self.__ospf_interface_config = YANGDynClass(base=ospf_interface_config.ospf_interface_config, is_container='container', presence=False, yang_name="ospf-interface-config", rest_name="ospf", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Open Shortest Path First (OSPF).', u'cli-incomplete-no': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'sort-priority': u'113', u'alt-name': u'ospf'}}, namespace='urn:brocade.com:mgmt:brocade-ospf', defining_module='brocade-ospf', yang_type='container', is_config=True)

  ospf_interface_config = __builtin__.property(_get_ospf_interface_config, _set_ospf_interface_config)


  _pyangbind_elements = {'ospf_interface_config': ospf_interface_config, }


