
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import duplicateWWN
class login_policy(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/fabric/login-policy. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: This function control the switch login configurations
- Allow FLOGI/FDISC duplicate port WWN to login into switch.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__duplicateWWN',)

  _yang_name = 'login-policy'
  _rest_name = 'login-policy'

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
    self.__duplicateWWN = YANGDynClass(base=duplicateWWN.duplicateWWN, is_container='container', yang_name="duplicateWWN", rest_name="duplicateWWN", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'info': u'Configure the DuplicateWWN login policy of a switch in fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)

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
      return [u'rbridge-id', u'fabric', u'login-policy']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'fabric', u'login-policy']

  def _get_duplicateWWN(self):
    """
    Getter method for duplicateWWN, mapped from YANG variable /rbridge_id/fabric/login_policy/duplicateWWN (container)

    YANG Description: It decides the DuplicateWWN login policy of a switch
in a fabric.The below mentioned policies are supported.
- old login will have precedence.(Default behavior)
- new or second(dup) login takes precedence.
    """
    return self.__duplicateWWN
      
  def _set_duplicateWWN(self, v, load=False):
    """
    Setter method for duplicateWWN, mapped from YANG variable /rbridge_id/fabric/login_policy/duplicateWWN (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_duplicateWWN is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_duplicateWWN() directly.

    YANG Description: It decides the DuplicateWWN login policy of a switch
in a fabric.The below mentioned policies are supported.
- old login will have precedence.(Default behavior)
- new or second(dup) login takes precedence.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=duplicateWWN.duplicateWWN, is_container='container', yang_name="duplicateWWN", rest_name="duplicateWWN", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'info': u'Configure the DuplicateWWN login policy of a switch in fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """duplicateWWN must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=duplicateWWN.duplicateWWN, is_container='container', yang_name="duplicateWWN", rest_name="duplicateWWN", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'info': u'Configure the DuplicateWWN login policy of a switch in fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)""",
        })

    self.__duplicateWWN = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_duplicateWWN(self):
    self.__duplicateWWN = YANGDynClass(base=duplicateWWN.duplicateWWN, is_container='container', yang_name="duplicateWWN", rest_name="duplicateWWN", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'info': u'Configure the DuplicateWWN login policy of a switch in fabric.'}}, namespace='urn:brocade.com:mgmt:brocade-fabric-service', defining_module='brocade-fabric-service', yang_type='container', is_config=True)

  duplicateWWN = __builtin__.property(_get_duplicateWWN, _set_duplicateWWN)


  _pyangbind_elements = {'duplicateWWN': duplicateWWN, }


