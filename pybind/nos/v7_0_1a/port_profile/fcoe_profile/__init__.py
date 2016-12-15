
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import fcoeport
class fcoe_profile(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-port-profile - based on the path /port-profile/fcoe-profile. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: The FCoE profile.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__fcoeport',)

  _yang_name = 'fcoe-profile'
  _rest_name = 'fcoe-profile'

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
    self.__fcoeport = YANGDynClass(base=fcoeport.fcoeport, is_container='container', yang_name="fcoeport", rest_name="fcoeport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the port to be an FCOE port', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

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
      return [u'port-profile', u'fcoe-profile']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'port-profile', u'fcoe-profile']

  def _get_fcoeport(self):
    """
    Getter method for fcoeport, mapped from YANG variable /port_profile/fcoe_profile/fcoeport (container)

    YANG Description: The port associated with this port profile
will act as an FCOE port.
    """
    return self.__fcoeport
      
  def _set_fcoeport(self, v, load=False):
    """
    Setter method for fcoeport, mapped from YANG variable /port_profile/fcoe_profile/fcoeport (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_fcoeport is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_fcoeport() directly.

    YANG Description: The port associated with this port profile
will act as an FCOE port.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=fcoeport.fcoeport, is_container='container', yang_name="fcoeport", rest_name="fcoeport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the port to be an FCOE port', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """fcoeport must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=fcoeport.fcoeport, is_container='container', yang_name="fcoeport", rest_name="fcoeport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the port to be an FCOE port', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)""",
        })

    self.__fcoeport = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_fcoeport(self):
    self.__fcoeport = YANGDynClass(base=fcoeport.fcoeport, is_container='container', yang_name="fcoeport", rest_name="fcoeport", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure the port to be an FCOE port', u'display-when': u'/vcsmode/vcs-mode = "true"'}}, namespace='urn:brocade.com:mgmt:brocade-port-profile', defining_module='brocade-port-profile', yang_type='container', is_config=True)

  fcoeport = __builtin__.property(_get_fcoeport, _set_fcoeport)


  _pyangbind_elements = {'fcoeport': fcoeport, }


