
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import pim
import mld
class ipv6(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mld-snooping - based on the path /mld-snooping/ipv6. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__pim','__mld',)

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
    self.__pim = YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 PIM snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)
    self.__mld = YANGDynClass(base=mld.mld, is_container='container', yang_name="mld", rest_name="mld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Listener Discovery (MLD) Snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)

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
      return [u'mld-snooping', u'ipv6']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'ipv6']

  def _get_pim(self):
    """
    Getter method for pim, mapped from YANG variable /mld_snooping/ipv6/pim (container)
    """
    return self.__pim
      
  def _set_pim(self, v, load=False):
    """
    Setter method for pim, mapped from YANG variable /mld_snooping/ipv6/pim (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_pim is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_pim() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 PIM snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """pim must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 PIM snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)""",
        })

    self.__pim = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_pim(self):
    self.__pim = YANGDynClass(base=pim.pim, is_container='container', yang_name="pim", rest_name="pim", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'ipv6 PIM snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)


  def _get_mld(self):
    """
    Getter method for mld, mapped from YANG variable /mld_snooping/ipv6/mld (container)
    """
    return self.__mld
      
  def _set_mld(self, v, load=False):
    """
    Setter method for mld, mapped from YANG variable /mld_snooping/ipv6/mld (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mld is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mld() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=mld.mld, is_container='container', yang_name="mld", rest_name="mld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Listener Discovery (MLD) Snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mld must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=mld.mld, is_container='container', yang_name="mld", rest_name="mld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Listener Discovery (MLD) Snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)""",
        })

    self.__mld = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mld(self):
    self.__mld = YANGDynClass(base=mld.mld, is_container='container', yang_name="mld", rest_name="mld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Multicast Listener Discovery (MLD) Snooping', u'callpoint': u'MldsGlobal', u'cli-incomplete-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mld-snooping', defining_module='brocade-mld-snooping', yang_type='container', is_config=True)

  pim = __builtin__.property(_get_pim, _set_pim)
  mld = __builtin__.property(_get_mld, _set_mld)


  _pyangbind_elements = {'pim': pim, 'mld': mld, }


