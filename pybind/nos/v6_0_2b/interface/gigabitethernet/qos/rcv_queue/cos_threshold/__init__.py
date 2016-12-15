
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class cos_threshold(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /interface/gigabitethernet/qos/rcv-queue/cos-threshold. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.

  YANG Description: Configure CoS Thresholds
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__cos0_threshold','__cos1_threshold','__cos2_threshold','__cos3_threshold','__cos4_threshold','__cos5_threshold','__cos6_threshold','__cos7_threshold',)

  _yang_name = 'cos-threshold'
  _rest_name = 'cos-threshold'

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
    self.__cos5_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos5-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos1_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos1-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos3_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos3-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos0_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos0-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos2_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos2-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos7_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos7-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos4_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos4-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    self.__cos6_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos6-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)

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
      return [u'interface', u'gigabitethernet', u'qos', u'rcv-queue', u'cos-threshold']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'interface', u'GigabitEthernet', u'qos', u'rcv-queue', u'cos-threshold']

  def _get_cos0_threshold(self):
    """
    Getter method for cos0_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos0_threshold (uint32)

    YANG Description: CoS 0 tail drop threshold
    """
    return self.__cos0_threshold
      
  def _set_cos0_threshold(self, v, load=False):
    """
    Setter method for cos0_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos0_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos0_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos0_threshold() directly.

    YANG Description: CoS 0 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos0-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos0_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos0-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos0_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos0_threshold(self):
    self.__cos0_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos0-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos1_threshold(self):
    """
    Getter method for cos1_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos1_threshold (uint32)

    YANG Description: CoS 1 tail drop threshold
    """
    return self.__cos1_threshold
      
  def _set_cos1_threshold(self, v, load=False):
    """
    Setter method for cos1_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos1_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos1_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos1_threshold() directly.

    YANG Description: CoS 1 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos1-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos1_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos1-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos1_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos1_threshold(self):
    self.__cos1_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos1-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos2_threshold(self):
    """
    Getter method for cos2_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos2_threshold (uint32)

    YANG Description: CoS 2 tail drop threshold
    """
    return self.__cos2_threshold
      
  def _set_cos2_threshold(self, v, load=False):
    """
    Setter method for cos2_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos2_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos2_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos2_threshold() directly.

    YANG Description: CoS 2 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos2-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos2_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos2-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos2_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos2_threshold(self):
    self.__cos2_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos2-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos3_threshold(self):
    """
    Getter method for cos3_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos3_threshold (uint32)

    YANG Description: CoS 3 tail drop threshold
    """
    return self.__cos3_threshold
      
  def _set_cos3_threshold(self, v, load=False):
    """
    Setter method for cos3_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos3_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos3_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos3_threshold() directly.

    YANG Description: CoS 3 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos3-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos3_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos3-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos3_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos3_threshold(self):
    self.__cos3_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos3-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos4_threshold(self):
    """
    Getter method for cos4_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos4_threshold (uint32)

    YANG Description: CoS 4 tail drop threshold
    """
    return self.__cos4_threshold
      
  def _set_cos4_threshold(self, v, load=False):
    """
    Setter method for cos4_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos4_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos4_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos4_threshold() directly.

    YANG Description: CoS 4 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos4-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos4_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos4-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos4_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos4_threshold(self):
    self.__cos4_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos4-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos5_threshold(self):
    """
    Getter method for cos5_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos5_threshold (uint32)

    YANG Description: CoS 5 tail drop threshold
    """
    return self.__cos5_threshold
      
  def _set_cos5_threshold(self, v, load=False):
    """
    Setter method for cos5_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos5_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos5_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos5_threshold() directly.

    YANG Description: CoS 5 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos5-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos5_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos5-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos5_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos5_threshold(self):
    self.__cos5_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos5-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos6_threshold(self):
    """
    Getter method for cos6_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos6_threshold (uint32)

    YANG Description: CoS 6 tail drop threshold
    """
    return self.__cos6_threshold
      
  def _set_cos6_threshold(self, v, load=False):
    """
    Setter method for cos6_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos6_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos6_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos6_threshold() directly.

    YANG Description: CoS 6 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos6-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos6_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos6-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos6_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos6_threshold(self):
    self.__cos6_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos6-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-incomplete-command': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)


  def _get_cos7_threshold(self):
    """
    Getter method for cos7_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos7_threshold (uint32)

    YANG Description: CoS 7 tail drop threshold
    """
    return self.__cos7_threshold
      
  def _set_cos7_threshold(self, v, load=False):
    """
    Setter method for cos7_threshold, mapped from YANG variable /interface/gigabitethernet/qos/rcv_queue/cos_threshold/cos7_threshold (uint32)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cos7_threshold is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cos7_threshold() directly.

    YANG Description: CoS 7 tail drop threshold
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos7-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cos7_threshold must be of a type compatible with uint32""",
          'defined-type': "uint32",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos7-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)""",
        })

    self.__cos7_threshold = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cos7_threshold(self):
    self.__cos7_threshold = YANGDynClass(base=RestrictedClassType(base_type=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), restriction_dict={'range': [u'0 .. 100']}), is_leaf=True, yang_name="cos7-threshold", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-drop-node-name': None, u'cli-suppress-no': None}}, namespace='urn:brocade.com:mgmt:brocade-qos', defining_module='brocade-qos', yang_type='uint32', is_config=True)

  cos0_threshold = __builtin__.property(_get_cos0_threshold, _set_cos0_threshold)
  cos1_threshold = __builtin__.property(_get_cos1_threshold, _set_cos1_threshold)
  cos2_threshold = __builtin__.property(_get_cos2_threshold, _set_cos2_threshold)
  cos3_threshold = __builtin__.property(_get_cos3_threshold, _set_cos3_threshold)
  cos4_threshold = __builtin__.property(_get_cos4_threshold, _set_cos4_threshold)
  cos5_threshold = __builtin__.property(_get_cos5_threshold, _set_cos5_threshold)
  cos6_threshold = __builtin__.property(_get_cos6_threshold, _set_cos6_threshold)
  cos7_threshold = __builtin__.property(_get_cos7_threshold, _set_cos7_threshold)


  _pyangbind_elements = {'cos0_threshold': cos0_threshold, 'cos1_threshold': cos1_threshold, 'cos2_threshold': cos2_threshold, 'cos3_threshold': cos3_threshold, 'cos4_threshold': cos4_threshold, 'cos5_threshold': cos5_threshold, 'cos6_threshold': cos6_threshold, 'cos7_threshold': cos7_threshold, }


