
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import lldp_neighbor_detail
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-lldp-ext - based on the path /brocade_lldp_ext_rpc/get-lldp-neighbor-detail/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__lldp_neighbor_detail','__has_more',)

  _yang_name = 'output'
  _rest_name = 'output'

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
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='boolean', is_config=True)
    self.__lldp_neighbor_detail = YANGDynClass(base=YANGListType("local_interface_name remote_interface_name",lldp_neighbor_detail.lldp_neighbor_detail, yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-interface-name remote-interface-name', extensions=None), is_container='list', yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='list', is_config=True)

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
      return [u'brocade_lldp_ext_rpc', u'get-lldp-neighbor-detail', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-lldp-neighbor-detail', u'output']

  def _get_lldp_neighbor_detail(self):
    """
    Getter method for lldp_neighbor_detail, mapped from YANG variable /brocade_lldp_ext_rpc/get_lldp_neighbor_detail/output/lldp_neighbor_detail (list)

    YANG Description: A list of lldp neighbor interface entries.
    """
    return self.__lldp_neighbor_detail
      
  def _set_lldp_neighbor_detail(self, v, load=False):
    """
    Setter method for lldp_neighbor_detail, mapped from YANG variable /brocade_lldp_ext_rpc/get_lldp_neighbor_detail/output/lldp_neighbor_detail (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lldp_neighbor_detail is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lldp_neighbor_detail() directly.

    YANG Description: A list of lldp neighbor interface entries.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("local_interface_name remote_interface_name",lldp_neighbor_detail.lldp_neighbor_detail, yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-interface-name remote-interface-name', extensions=None), is_container='list', yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lldp_neighbor_detail must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("local_interface_name remote_interface_name",lldp_neighbor_detail.lldp_neighbor_detail, yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-interface-name remote-interface-name', extensions=None), is_container='list', yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='list', is_config=True)""",
        })

    self.__lldp_neighbor_detail = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lldp_neighbor_detail(self):
    self.__lldp_neighbor_detail = YANGDynClass(base=YANGListType("local_interface_name remote_interface_name",lldp_neighbor_detail.lldp_neighbor_detail, yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='local-interface-name remote-interface-name', extensions=None), is_container='list', yang_name="lldp-neighbor-detail", rest_name="lldp-neighbor-detail", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='list', is_config=True)


  def _get_has_more(self):
    """
    Getter method for has_more, mapped from YANG variable /brocade_lldp_ext_rpc/get_lldp_neighbor_detail/output/has_more (boolean)

    YANG Description: Informs whether there has more records that
are not part of current response. Based on this
flag remaining records can be fetched with
another request by giving IfIndex of last
interface received in response
    """
    return self.__has_more
      
  def _set_has_more(self, v, load=False):
    """
    Setter method for has_more, mapped from YANG variable /brocade_lldp_ext_rpc/get_lldp_neighbor_detail/output/has_more (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_has_more is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_has_more() directly.

    YANG Description: Informs whether there has more records that
are not part of current response. Based on this
flag remaining records can be fetched with
another request by giving IfIndex of last
interface received in response
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """has_more must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='boolean', is_config=True)""",
        })

    self.__has_more = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_has_more(self):
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-lldp-ext', defining_module='brocade-lldp-ext', yang_type='boolean', is_config=True)

  lldp_neighbor_detail = __builtin__.property(_get_lldp_neighbor_detail, _set_lldp_neighbor_detail)
  has_more = __builtin__.property(_get_has_more, _set_has_more)


  _pyangbind_elements = {'lldp_neighbor_detail': lldp_neighbor_detail, 'has_more': has_more, }


