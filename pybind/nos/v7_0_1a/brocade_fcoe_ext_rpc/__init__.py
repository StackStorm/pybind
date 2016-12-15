
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcoe_get_interface
import fcoe_get_login
class brocade_fcoe_ext(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-fcoe-ext - based on the path /brocade_fcoe_ext_rpc. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This management module is an extension to FCOE model for
    - Defining RPCs to retrieve operational information of 
      the FCoE.
        
Glossary of the terms used:
---------------------------
ACC frame - Accept frame

FCoE -      Fibre Channel over Ethernet (FCoE) is an 
           encapsulation of Fibre Channel frames over Ethernet
           networks. 

FIP -       FCoE Intialization Protocol is the standard for 
           intilization of FCoE network.

FCF -       Fibre Channel Forwarder is a network entity 
           responsible for forwarding the FCoE traffic.

FLOGI -     Fabric Login is a frame used by the end devices to 
           login to a Fibre Channel or FCoE Fabric.

FDISC -     Fabric Discovery is a frame used by the end devices 
           to perform logins of all the loop attached ports.

LOGO -      Logout is a frame used by the end devices to logout 
           of the Fibre Channel or FCoE Fabric.

ENODE -     End Node is the term used to refer End devices in 
           the FCoE network.

VN-Port -   Virtual N-Port is the FCoE equivalent of the Fibre 
           Channel N-Port.

CVL -       Clear Virtual Links is the frame to tear the Virtual
           Links in the FCoE Network.

  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoe_get_interface','__fcoe_get_login',)

  _yang_name = 'brocade-fcoe-ext'
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
    self.__fcoe_get_login = YANGDynClass(base=fcoe_get_login.fcoe_get_login, is_leaf=True, yang_name="fcoe-get-login", rest_name="fcoe-get-login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)
    self.__fcoe_get_interface = YANGDynClass(base=fcoe_get_interface.fcoe_get_interface, is_leaf=True, yang_name="fcoe-get-interface", rest_name="fcoe-get-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)

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
      return [u'brocade_fcoe_ext_rpc']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return []

  def _get_fcoe_get_interface(self):
    """
    Getter method for fcoe_get_interface, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface (rpc)

    YANG Description: This function is to get the operational state of an FCoE
interface(s).
    """
    return self.__fcoe_get_interface
      
  def _set_fcoe_get_interface(self, v, load=False):
    """
    Setter method for fcoe_get_interface, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_interface (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_get_interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_get_interface() directly.

    YANG Description: This function is to get the operational state of an FCoE
interface(s).
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcoe_get_interface.fcoe_get_interface, is_leaf=True, yang_name="fcoe-get-interface", rest_name="fcoe-get-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_get_interface must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=fcoe_get_interface.fcoe_get_interface, is_leaf=True, yang_name="fcoe-get-interface", rest_name="fcoe-get-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)""",
        })

    self.__fcoe_get_interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_get_interface(self):
    self.__fcoe_get_interface = YANGDynClass(base=fcoe_get_interface.fcoe_get_interface, is_leaf=True, yang_name="fcoe-get-interface", rest_name="fcoe-get-interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)


  def _get_fcoe_get_login(self):
    """
    Getter method for fcoe_get_login, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_login (rpc)

    YANG Description: This function provides the login information on FCoE 
End nodes that have logged in to the managed device.
    """
    return self.__fcoe_get_login
      
  def _set_fcoe_get_login(self, v, load=False):
    """
    Setter method for fcoe_get_login, mapped from YANG variable /brocade_fcoe_ext_rpc/fcoe_get_login (rpc)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoe_get_login is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoe_get_login() directly.

    YANG Description: This function provides the login information on FCoE 
End nodes that have logged in to the managed device.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcoe_get_login.fcoe_get_login, is_leaf=True, yang_name="fcoe-get-login", rest_name="fcoe-get-login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoe_get_login must be of a type compatible with rpc""",
          'defined-type': "rpc",
          'generated-type': """YANGDynClass(base=fcoe_get_login.fcoe_get_login, is_leaf=True, yang_name="fcoe-get-login", rest_name="fcoe-get-login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)""",
        })

    self.__fcoe_get_login = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoe_get_login(self):
    self.__fcoe_get_login = YANGDynClass(base=fcoe_get_login.fcoe_get_login, is_leaf=True, yang_name="fcoe-get-login", rest_name="fcoe-get-login", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions={u'tailf-common': {u'hidden': u'rpccmd', u'actionpoint': u'fcoe-show-action-point'}}, namespace='urn:brocade.com:mgmt:brocade-fcoe-ext', defining_module='brocade-fcoe-ext', yang_type='rpc', is_config=True)

  fcoe_get_interface = __builtin__.property(_get_fcoe_get_interface, _set_fcoe_get_interface)
  fcoe_get_login = __builtin__.property(_get_fcoe_get_login, _set_fcoe_get_login)


  _pyangbind_elements = {'fcoe_get_interface': fcoe_get_interface, 'fcoe_get_login': fcoe_get_login, }


