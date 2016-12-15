
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-system-capabilities - based on the path /capabilities/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__ipv6Raguard',)

  _yang_name = 'ipv6'
  _rest_name = 'ipv6'

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
    self.__ipv6Raguard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6Raguard", rest_name="ipv6Raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)

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
      return [u'capabilities', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'capabilities', u'ipv6']

  def _get_ipv6Raguard(self):
    """
    Getter method for ipv6Raguard, mapped from YANG variable /capabilities/ipv6/ipv6Raguard (boolean)
    """
    return self.__ipv6Raguard
      
  def _set_ipv6Raguard(self, v, load=False):
    """
    Setter method for ipv6Raguard, mapped from YANG variable /capabilities/ipv6/ipv6Raguard (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_ipv6Raguard is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_ipv6Raguard() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="ipv6Raguard", rest_name="ipv6Raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """ipv6Raguard must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6Raguard", rest_name="ipv6Raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)""",
        })

    self.__ipv6Raguard = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_ipv6Raguard(self):
    self.__ipv6Raguard = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="ipv6Raguard", rest_name="ipv6Raguard", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:brocade.com:mgmt:brocade-system-capabilities', defining_module='brocade-system-capabilities', yang_type='boolean', is_config=False)

  ipv6Raguard = __builtin__.property(_get_ipv6Raguard)


  _pyangbind_elements = {'ipv6Raguard': ipv6Raguard, }


