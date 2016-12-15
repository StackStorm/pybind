
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import root_bridge
import bridge
import port
class stp(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-brief-info/output/spanning-tree-info/stp. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__root_bridge','__bridge','__port',)

  _yang_name = 'stp'
  _rest_name = 'stp'

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
    self.__bridge = YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__root_bridge = YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'stp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-brief-info', u'output', u'spanning-tree-info', u'stp']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-brief-info', u'output', u'spanning-tree-info', u'stp']

  def _get_root_bridge(self):
    """
    Getter method for root_bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge (container)
    """
    return self.__root_bridge
      
  def _set_root_bridge(self, v, load=False):
    """
    Setter method for root_bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/root_bridge (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_root_bridge is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_root_bridge() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """root_bridge must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__root_bridge = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_root_bridge(self):
    self.__root_bridge = YANGDynClass(base=root_bridge.root_bridge, is_container='container', yang_name="root-bridge", rest_name="root-bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_bridge(self):
    """
    Getter method for bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/bridge (container)
    """
    return self.__bridge
      
  def _set_bridge(self, v, load=False):
    """
    Setter method for bridge, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/bridge (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bridge is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bridge() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bridge must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__bridge = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bridge(self):
    self.__bridge = YANGDynClass(base=bridge.bridge, is_container='container', yang_name="bridge", rest_name="bridge", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_port(self):
    """
    Getter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/port (list)
    """
    return self.__port
      
  def _set_port(self, v, load=False):
    """
    Setter method for port, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_brief_info/output/spanning_tree_info/stp/port (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_port is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_port() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'stp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """port must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'stp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__port = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_port(self):
    self.__port = YANGDynClass(base=YANGListType(False,port.port, yang_name="port", rest_name="port", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None, choice=(u'spanning-tree-mode', u'stp')), is_container='list', yang_name="port", rest_name="port", parent=self, choice=(u'spanning-tree-mode', u'stp'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

  root_bridge = __builtin__.property(_get_root_bridge, _set_root_bridge)
  bridge = __builtin__.property(_get_bridge, _set_bridge)
  port = __builtin__.property(_get_port, _set_port)

  __choices__ = {u'spanning-tree-mode': {u'stp': [u'root_bridge', u'bridge', u'port']}}
  _pyangbind_elements = {'root_bridge': root_bridge, 'bridge': bridge, 'port': port, }


