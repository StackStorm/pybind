
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class input(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-isns-ext - based on the path /brocade_isns_ext_rpc/isns-get-discovery-domain-set/input. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__isns_dds_name',)

  _yang_name = 'input'
  _rest_name = 'input'

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
    self.__isns_dds_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-dds-name", rest_name="isns-dds-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-dds-name-type', is_config=True)

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
      return [u'brocade_isns_ext_rpc', u'isns-get-discovery-domain-set', u'input']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'isns-get-discovery-domain-set', u'input']

  def _get_isns_dds_name(self):
    """
    Getter method for isns_dds_name, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_discovery_domain_set/input/isns_dds_name (isns:isns-dds-name-type)

    YANG Description: This specifies the name for the Discovery Domain Set.
    """
    return self.__isns_dds_name
      
  def _set_isns_dds_name(self, v, load=False):
    """
    Setter method for isns_dds_name, mapped from YANG variable /brocade_isns_ext_rpc/isns_get_discovery_domain_set/input/isns_dds_name (isns:isns-dds-name-type)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_isns_dds_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_isns_dds_name() directly.

    YANG Description: This specifies the name for the Discovery Domain Set.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-dds-name", rest_name="isns-dds-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-dds-name-type', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """isns_dds_name must be of a type compatible with isns:isns-dds-name-type""",
          'defined-type': "isns:isns-dds-name-type",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-dds-name", rest_name="isns-dds-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-dds-name-type', is_config=True)""",
        })

    self.__isns_dds_name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_isns_dds_name(self):
    self.__isns_dds_name = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'[-_0-9a-zA-Z]{1,255}', 'length': [u'1..255']}), is_leaf=True, yang_name="isns-dds-name", rest_name="isns-dds-name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-isns-ext', defining_module='brocade-isns-ext', yang_type='isns:isns-dds-name-type', is_config=True)

  isns_dds_name = __builtin__.property(_get_isns_dds_name, _set_isns_dds_name)


  _pyangbind_elements = {'isns_dds_name': isns_dds_name, }


