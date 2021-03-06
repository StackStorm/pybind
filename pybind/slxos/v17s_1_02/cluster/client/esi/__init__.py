
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class esi(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mct - based on the path /cluster/client/esi. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Ethernet Segment Id
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__esi_value','__esi_auto',)

  _yang_name = 'esi'
  _rest_name = 'esi'

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
    self.__esi_value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})(;[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})*'}), is_leaf=True, yang_name="esi-value", rest_name="esi-value", parent=self, choice=(u'esi', u'esi-ch-val'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster client ESI HH:HH:HH:HH:HH:HH:HH:HH:HH', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='cluster-client-esi', is_config=True)
    self.__esi_auto = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'lacp': {'value': 1}},), is_leaf=True, yang_name="esi-auto", rest_name="auto", parent=self, choice=(u'esi', u'esi-ch-auto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Esi auto set', u'cli-full-command': None, u'alt-name': u'auto', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)

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
      return [u'cluster', u'client', u'esi']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'cluster', u'client', u'esi']

  def _get_esi_value(self):
    """
    Getter method for esi_value, mapped from YANG variable /cluster/client/esi/esi_value (cluster-client-esi)
    """
    return self.__esi_value
      
  def _set_esi_value(self, v, load=False):
    """
    Setter method for esi_value, mapped from YANG variable /cluster/client/esi/esi_value (cluster-client-esi)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_esi_value is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_esi_value() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})(;[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})*'}), is_leaf=True, yang_name="esi-value", rest_name="esi-value", parent=self, choice=(u'esi', u'esi-ch-val'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster client ESI HH:HH:HH:HH:HH:HH:HH:HH:HH', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='cluster-client-esi', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """esi_value must be of a type compatible with cluster-client-esi""",
          'defined-type': "brocade-mct:cluster-client-esi",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})(;[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})*'}), is_leaf=True, yang_name="esi-value", rest_name="esi-value", parent=self, choice=(u'esi', u'esi-ch-val'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster client ESI HH:HH:HH:HH:HH:HH:HH:HH:HH', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='cluster-client-esi', is_config=True)""",
        })

    self.__esi_value = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_esi_value(self):
    self.__esi_value = YANGDynClass(base=RestrictedClassType(base_type=unicode, restriction_dict={'pattern': u'([0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})(;[0-9a-fA-F]{1,2}(:[0-9a-fA-F]{1,2}){2,8})*'}), is_leaf=True, yang_name="esi-value", rest_name="esi-value", parent=self, choice=(u'esi', u'esi-ch-val'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Cluster client ESI HH:HH:HH:HH:HH:HH:HH:HH:HH', u'cli-drop-node-name': None, u'cli-full-no': None, u'cli-full-command': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='cluster-client-esi', is_config=True)


  def _get_esi_auto(self):
    """
    Getter method for esi_auto, mapped from YANG variable /cluster/client/esi/esi_auto (enumeration)
    """
    return self.__esi_auto
      
  def _set_esi_auto(self, v, load=False):
    """
    Setter method for esi_auto, mapped from YANG variable /cluster/client/esi/esi_auto (enumeration)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_esi_auto is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_esi_auto() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'lacp': {'value': 1}},), is_leaf=True, yang_name="esi-auto", rest_name="auto", parent=self, choice=(u'esi', u'esi-ch-auto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Esi auto set', u'cli-full-command': None, u'alt-name': u'auto', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """esi_auto must be of a type compatible with enumeration""",
          'defined-type': "brocade-mct:enumeration",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'lacp': {'value': 1}},), is_leaf=True, yang_name="esi-auto", rest_name="auto", parent=self, choice=(u'esi', u'esi-ch-auto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Esi auto set', u'cli-full-command': None, u'alt-name': u'auto', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)""",
        })

    self.__esi_auto = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_esi_auto(self):
    self.__esi_auto = YANGDynClass(base=RestrictedClassType(base_type=unicode,                                     restriction_type="dict_key",                                     restriction_arg={u'lacp': {'value': 1}},), is_leaf=True, yang_name="esi-auto", rest_name="auto", parent=self, choice=(u'esi', u'esi-ch-auto'), path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Esi auto set', u'cli-full-command': None, u'alt-name': u'auto', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-mct', defining_module='brocade-mct', yang_type='enumeration', is_config=True)

  esi_value = __builtin__.property(_get_esi_value, _set_esi_value)
  esi_auto = __builtin__.property(_get_esi_auto, _set_esi_auto)

  __choices__ = {u'esi': {u'esi-ch-auto': [u'esi_auto'], u'esi-ch-val': [u'esi_value']}}
  _pyangbind_elements = {'esi_value': esi_value, 'esi_auto': esi_auto, }


