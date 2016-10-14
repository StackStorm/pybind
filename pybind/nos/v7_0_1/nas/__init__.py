
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import auto_qos
import server_ip
class nas(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-qos - based on the path /nas. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__auto_qos','__server_ip',)

  _yang_name = 'nas'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    helper = kwargs.pop("path_helper", None)
    if helper is False:
      self._path_helper = False
    elif helper is not None and isinstance(helper, xpathhelper.YANGPathHelper):
      self._path_helper = helper
    elif hasattr(self, "_parent"):
      helper = getattr(self._parent, "_path_helper", False)
      self._path_helper = helper
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
    self.__server_ip = YANGDynClass(base=YANGListType("server_ip",server_ip.server_ip, yang_name="server-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='server-ip', extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}), is_container='list', yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    self.__auto_qos = YANGDynClass(base=auto_qos.auto_qos, is_container='container', yang_name="auto-qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'info': u'Automatic Quality Of Service', u'callpoint': u'qos_nas_config'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)

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
      return [u'nas']

  def _rest_path(self):
    if hasattr(self, "_supplied_register_path"):
      return [self._supplied_register_path]
    if hasattr(self, "_parent"):
      return self._parent._rest_path()+[self._yang_name]
    else:
      return [u'nas']

  def _get_auto_qos(self):
    """
    Getter method for auto_qos, mapped from YANG variable /nas/auto_qos (container)

    YANG Description: This specifies Automatic Quality Of Service 
parameters
    """
    return self.__auto_qos
      
  def _set_auto_qos(self, v, load=False):
    """
    Setter method for auto_qos, mapped from YANG variable /nas/auto_qos (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_auto_qos is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_auto_qos() directly.

    YANG Description: This specifies Automatic Quality Of Service 
parameters
    """
    try:
      t = YANGDynClass(v,base=auto_qos.auto_qos, is_container='container', yang_name="auto-qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'info': u'Automatic Quality Of Service', u'callpoint': u'qos_nas_config'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """auto_qos must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=auto_qos.auto_qos, is_container='container', yang_name="auto-qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'info': u'Automatic Quality Of Service', u'callpoint': u'qos_nas_config'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)""",
        })

    self.__auto_qos = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_auto_qos(self):
    self.__auto_qos = YANGDynClass(base=auto_qos.auto_qos, is_container='container', yang_name="auto-qos", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'cli-full-no': None, u'info': u'Automatic Quality Of Service', u'callpoint': u'qos_nas_config'}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='container', is_config=True)


  def _get_server_ip(self):
    """
    Getter method for server_ip, mapped from YANG variable /nas/server_ip (list)
    """
    return self.__server_ip
      
  def _set_server_ip(self, v, load=False):
    """
    Setter method for server_ip, mapped from YANG variable /nas/server_ip (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_server_ip is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_server_ip() directly.
    """
    try:
      t = YANGDynClass(v,base=YANGListType("server_ip",server_ip.server_ip, yang_name="server-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='server-ip', extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}), is_container='list', yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """server_ip must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("server_ip",server_ip.server_ip, yang_name="server-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='server-ip', extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}), is_container='list', yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)""",
        })

    self.__server_ip = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_server_ip(self):
    self.__server_ip = YANGDynClass(base=YANGListType("server_ip",server_ip.server_ip, yang_name="server-ip", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='server-ip', extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}), is_container='list', yang_name="server-ip", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'NAS server', u'cli-suppress-mode': None, u'cli-no-key-completion': None, u'callpoint': u'qos_nas_serverip', u'cli-suppress-list-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='list', is_config=True)

  auto_qos = __builtin__.property(_get_auto_qos, _set_auto_qos)
  server_ip = __builtin__.property(_get_server_ip, _set_server_ip)


  _pyangbind_elements = {'auto_qos': auto_qos, 'server_ip': server_ip, }

