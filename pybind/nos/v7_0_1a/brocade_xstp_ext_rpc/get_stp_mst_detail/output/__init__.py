
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cist
import msti
import last_instance
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-xstp-ext - based on the path /brocade_xstp_ext_rpc/get-stp-mst-detail/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cist','__msti','__has_more','__last_instance',)

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
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='boolean', is_config=True)
    self.__cist = YANGDynClass(base=cist.cist, is_container='container', yang_name="cist", rest_name="cist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__last_instance = YANGDynClass(base=last_instance.last_instance, is_container='container', yang_name="last-instance", rest_name="last-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    self.__msti = YANGDynClass(base=YANGListType("instance_id",msti.msti, yang_name="msti", rest_name="msti", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="msti", rest_name="msti", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)

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
      return [u'brocade_xstp_ext_rpc', u'get-stp-mst-detail', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'get-stp-mst-detail', u'output']

  def _get_cist(self):
    """
    Getter method for cist, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/cist (container)
    """
    return self.__cist
      
  def _set_cist(self, v, load=False):
    """
    Setter method for cist, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/cist (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cist is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cist() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cist.cist, is_container='container', yang_name="cist", rest_name="cist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cist must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cist.cist, is_container='container', yang_name="cist", rest_name="cist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__cist = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cist(self):
    self.__cist = YANGDynClass(base=cist.cist, is_container='container', yang_name="cist", rest_name="cist", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)


  def _get_msti(self):
    """
    Getter method for msti, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti (list)
    """
    return self.__msti
      
  def _set_msti(self, v, load=False):
    """
    Setter method for msti, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/msti (list)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_msti is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_msti() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGListType("instance_id",msti.msti, yang_name="msti", rest_name="msti", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="msti", rest_name="msti", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """msti must be of a type compatible with list""",
          'defined-type': "list",
          'generated-type': """YANGDynClass(base=YANGListType("instance_id",msti.msti, yang_name="msti", rest_name="msti", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="msti", rest_name="msti", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)""",
        })

    self.__msti = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_msti(self):
    self.__msti = YANGDynClass(base=YANGListType("instance_id",msti.msti, yang_name="msti", rest_name="msti", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='instance-id', extensions=None), is_container='list', yang_name="msti", rest_name="msti", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='list', is_config=True)


  def _get_has_more(self):
    """
    Getter method for has_more, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/has_more (boolean)

    YANG Description: Indicates if this response is complete or not. Value 
'true' indicates that the response is partial and there
are more spanning-tree instances. Clients can retrieve
next set of instances by passing the last received
instance id (from ../last-instance/instance-id) in the
subsequent RPC call.
    """
    return self.__has_more
      
  def _set_has_more(self, v, load=False):
    """
    Setter method for has_more, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/has_more (boolean)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_has_more is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_has_more() directly.

    YANG Description: Indicates if this response is complete or not. Value 
'true' indicates that the response is partial and there
are more spanning-tree instances. Clients can retrieve
next set of instances by passing the last received
instance id (from ../last-instance/instance-id) in the
subsequent RPC call.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='boolean', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """has_more must be of a type compatible with boolean""",
          'defined-type': "boolean",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='boolean', is_config=True)""",
        })

    self.__has_more = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_has_more(self):
    self.__has_more = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="has-more", rest_name="has-more", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='boolean', is_config=True)


  def _get_last_instance(self):
    """
    Getter method for last_instance, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/last_instance (container)

    YANG Description: The 'last' spanning-tree instance included in this
response.
    """
    return self.__last_instance
      
  def _set_last_instance(self, v, load=False):
    """
    Setter method for last_instance, mapped from YANG variable /brocade_xstp_ext_rpc/get_stp_mst_detail/output/last_instance (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_last_instance is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_last_instance() directly.

    YANG Description: The 'last' spanning-tree instance included in this
response.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=last_instance.last_instance, is_container='container', yang_name="last-instance", rest_name="last-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """last_instance must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=last_instance.last_instance, is_container='container', yang_name="last-instance", rest_name="last-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)""",
        })

    self.__last_instance = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_last_instance(self):
    self.__last_instance = YANGDynClass(base=last_instance.last_instance, is_container='container', yang_name="last-instance", rest_name="last-instance", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:brocade.com:mgmt:brocade-xstp-ext', defining_module='brocade-xstp-ext', yang_type='container', is_config=True)

  cist = __builtin__.property(_get_cist, _set_cist)
  msti = __builtin__.property(_get_msti, _set_msti)
  has_more = __builtin__.property(_get_has_more, _set_has_more)
  last_instance = __builtin__.property(_get_last_instance, _set_last_instance)


  _pyangbind_elements = {'cist': cist, 'msti': msti, 'has_more': has_more, 'last_instance': last_instance, }


