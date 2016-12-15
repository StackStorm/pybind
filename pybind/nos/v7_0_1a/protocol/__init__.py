
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import edge_loop_detection
import lldp
import udld
import spanning_tree
class protocol(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-interface - based on the path /protocol. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__edge_loop_detection','__lldp','__udld','__spanning_tree',)

  _yang_name = 'protocol'
  _rest_name = 'protocol'

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
    self.__lldp = YANGDynClass(base=lldp.lldp, is_container='container', yang_name="lldp", rest_name="lldp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link Layer Discovery Protocol(LLDP)', u'callpoint': u'lldp_global_conf', u'sort-priority': u'52', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'conf-lldp'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    self.__spanning_tree = YANGDynClass(base=spanning_tree.spanning_tree, is_container='container', yang_name="spanning-tree", rest_name="spanning-tree", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree commands', u'cli-full-no': None, u'sort-priority': u'51'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    self.__edge_loop_detection = YANGDynClass(base=edge_loop_detection.edge_loop_detection, is_container='container', yang_name="edge-loop-detection", rest_name="edge-loop-detection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ELD parameters', u'callpoint': u'eld_system', u'sort-priority': u'57', u'cli-suppress-no': None, u'cli-full-command': None, u'cli-add-mode': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-mode-name': u'conf-eld'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)
    self.__udld = YANGDynClass(base=udld.udld, is_container='container', yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'UdldConfig', u'info': u'Unidirectional Link Detection protocol', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='container', is_config=True)

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
      return [u'protocol']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'protocol']

  def _get_edge_loop_detection(self):
    """
    Getter method for edge_loop_detection, mapped from YANG variable /protocol/edge_loop_detection (container)
    """
    return self.__edge_loop_detection
      
  def _set_edge_loop_detection(self, v, load=False):
    """
    Setter method for edge_loop_detection, mapped from YANG variable /protocol/edge_loop_detection (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_edge_loop_detection is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_edge_loop_detection() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=edge_loop_detection.edge_loop_detection, is_container='container', yang_name="edge-loop-detection", rest_name="edge-loop-detection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ELD parameters', u'callpoint': u'eld_system', u'sort-priority': u'57', u'cli-suppress-no': None, u'cli-full-command': None, u'cli-add-mode': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-mode-name': u'conf-eld'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """edge_loop_detection must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=edge_loop_detection.edge_loop_detection, is_container='container', yang_name="edge-loop-detection", rest_name="edge-loop-detection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ELD parameters', u'callpoint': u'eld_system', u'sort-priority': u'57', u'cli-suppress-no': None, u'cli-full-command': None, u'cli-add-mode': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-mode-name': u'conf-eld'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)""",
        })

    self.__edge_loop_detection = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_edge_loop_detection(self):
    self.__edge_loop_detection = YANGDynClass(base=edge_loop_detection.edge_loop_detection, is_container='container', yang_name="edge-loop-detection", rest_name="edge-loop-detection", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Configure ELD parameters', u'callpoint': u'eld_system', u'sort-priority': u'57', u'cli-suppress-no': None, u'cli-full-command': None, u'cli-add-mode': None, u'display-when': u'/vcsmode/vcs-mode = "true"', u'cli-mode-name': u'conf-eld'}}, namespace='urn:brocade.com:mgmt:brocade-eld', defining_module='brocade-eld', yang_type='container', is_config=True)


  def _get_lldp(self):
    """
    Getter method for lldp, mapped from YANG variable /protocol/lldp (container)
    """
    return self.__lldp
      
  def _set_lldp(self, v, load=False):
    """
    Setter method for lldp, mapped from YANG variable /protocol/lldp (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_lldp is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_lldp() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=lldp.lldp, is_container='container', yang_name="lldp", rest_name="lldp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link Layer Discovery Protocol(LLDP)', u'callpoint': u'lldp_global_conf', u'sort-priority': u'52', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'conf-lldp'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """lldp must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=lldp.lldp, is_container='container', yang_name="lldp", rest_name="lldp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link Layer Discovery Protocol(LLDP)', u'callpoint': u'lldp_global_conf', u'sort-priority': u'52', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'conf-lldp'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)""",
        })

    self.__lldp = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_lldp(self):
    self.__lldp = YANGDynClass(base=lldp.lldp, is_container='container', yang_name="lldp", rest_name="lldp", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Link Layer Discovery Protocol(LLDP)', u'callpoint': u'lldp_global_conf', u'sort-priority': u'52', u'cli-full-command': None, u'cli-add-mode': None, u'cli-full-no': None, u'cli-mode-name': u'conf-lldp'}}, namespace='urn:brocade.com:mgmt:brocade-lldp', defining_module='brocade-lldp', yang_type='container', is_config=True)


  def _get_udld(self):
    """
    Getter method for udld, mapped from YANG variable /protocol/udld (container)

    YANG Description: UDLD protocol configuration. UDLD protocol will be
enabled when '/protocol/udld' container is created. To
disable delete it or set '/protocol/udld/shutdown'
leaf
    """
    return self.__udld
      
  def _set_udld(self, v, load=False):
    """
    Setter method for udld, mapped from YANG variable /protocol/udld (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_udld is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_udld() directly.

    YANG Description: UDLD protocol configuration. UDLD protocol will be
enabled when '/protocol/udld' container is created. To
disable delete it or set '/protocol/udld/shutdown'
leaf
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=udld.udld, is_container='container', yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'UdldConfig', u'info': u'Unidirectional Link Detection protocol', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """udld must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=udld.udld, is_container='container', yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'UdldConfig', u'info': u'Unidirectional Link Detection protocol', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='container', is_config=True)""",
        })

    self.__udld = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_udld(self):
    self.__udld = YANGDynClass(base=udld.udld, is_container='container', yang_name="udld", rest_name="udld", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-add-mode': None, u'cli-full-command': None, u'callpoint': u'UdldConfig', u'info': u'Unidirectional Link Detection protocol', u'cli-full-no': None}}, namespace='urn:brocade.com:mgmt:brocade-udld', defining_module='brocade-udld', yang_type='container', is_config=True)


  def _get_spanning_tree(self):
    """
    Getter method for spanning_tree, mapped from YANG variable /protocol/spanning_tree (container)
    """
    return self.__spanning_tree
      
  def _set_spanning_tree(self, v, load=False):
    """
    Setter method for spanning_tree, mapped from YANG variable /protocol/spanning_tree (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_spanning_tree is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_spanning_tree() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=spanning_tree.spanning_tree, is_container='container', yang_name="spanning-tree", rest_name="spanning-tree", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree commands', u'cli-full-no': None, u'sort-priority': u'51'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """spanning_tree must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=spanning_tree.spanning_tree, is_container='container', yang_name="spanning-tree", rest_name="spanning-tree", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree commands', u'cli-full-no': None, u'sort-priority': u'51'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)""",
        })

    self.__spanning_tree = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_spanning_tree(self):
    self.__spanning_tree = YANGDynClass(base=spanning_tree.spanning_tree, is_container='container', yang_name="spanning-tree", rest_name="spanning-tree", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Spanning tree commands', u'cli-full-no': None, u'sort-priority': u'51'}}, namespace='urn:brocade.com:mgmt:brocade-xstp', defining_module='brocade-xstp', yang_type='container', is_config=True)

  edge_loop_detection = __builtin__.property(_get_edge_loop_detection, _set_edge_loop_detection)
  lldp = __builtin__.property(_get_lldp, _set_lldp)
  udld = __builtin__.property(_get_udld, _set_udld)
  spanning_tree = __builtin__.property(_get_spanning_tree, _set_spanning_tree)


  _pyangbind_elements = {'edge_loop_detection': edge_loop_detection, 'lldp': lldp, 'udld': udld, 'spanning_tree': spanning_tree, }


