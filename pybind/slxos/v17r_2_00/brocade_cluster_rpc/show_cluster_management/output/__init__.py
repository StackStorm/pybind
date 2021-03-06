
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import cluster_nodes
class output(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-cluster - based on the path /brocade_cluster_rpc/show-cluster-management/output. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__principal_switch_mac','__total_nodes_in_cluster','__nodes_disconnected_from_cluster','__cluster_nodes',)

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
    self.__cluster_nodes = YANGDynClass(base=cluster_nodes.cluster_nodes, is_container='container', presence=False, yang_name="cluster-nodes", rest_name="cluster-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='container', is_config=True)
    self.__total_nodes_in_cluster = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="total-nodes-in-cluster", rest_name="total-nodes-in-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)
    self.__principal_switch_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-mac", rest_name="principal-switch-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='string', is_config=True)
    self.__nodes_disconnected_from_cluster = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="nodes-disconnected-from-cluster", rest_name="nodes-disconnected-from-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)

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
      return [u'brocade_cluster_rpc', u'show-cluster-management', u'output']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'show-cluster-management', u'output']

  def _get_principal_switch_mac(self):
    """
    Getter method for principal_switch_mac, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/principal_switch_mac (string)

    YANG Description: Management Cluster Co-ordinator node MAC
    """
    return self.__principal_switch_mac
      
  def _set_principal_switch_mac(self, v, load=False):
    """
    Setter method for principal_switch_mac, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/principal_switch_mac (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_principal_switch_mac is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_principal_switch_mac() directly.

    YANG Description: Management Cluster Co-ordinator node MAC
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="principal-switch-mac", rest_name="principal-switch-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """principal_switch_mac must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-mac", rest_name="principal-switch-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='string', is_config=True)""",
        })

    self.__principal_switch_mac = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_principal_switch_mac(self):
    self.__principal_switch_mac = YANGDynClass(base=unicode, is_leaf=True, yang_name="principal-switch-mac", rest_name="principal-switch-mac", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='string', is_config=True)


  def _get_total_nodes_in_cluster(self):
    """
    Getter method for total_nodes_in_cluster, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/total_nodes_in_cluster (uint16)

    YANG Description: Total number of nodes in cluster
    """
    return self.__total_nodes_in_cluster
      
  def _set_total_nodes_in_cluster(self, v, load=False):
    """
    Setter method for total_nodes_in_cluster, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/total_nodes_in_cluster (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_total_nodes_in_cluster is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_total_nodes_in_cluster() directly.

    YANG Description: Total number of nodes in cluster
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="total-nodes-in-cluster", rest_name="total-nodes-in-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """total_nodes_in_cluster must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="total-nodes-in-cluster", rest_name="total-nodes-in-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)""",
        })

    self.__total_nodes_in_cluster = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_total_nodes_in_cluster(self):
    self.__total_nodes_in_cluster = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="total-nodes-in-cluster", rest_name="total-nodes-in-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)


  def _get_nodes_disconnected_from_cluster(self):
    """
    Getter method for nodes_disconnected_from_cluster, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/nodes_disconnected_from_cluster (uint16)

    YANG Description: Number of nodes disconnected from cluster
    """
    return self.__nodes_disconnected_from_cluster
      
  def _set_nodes_disconnected_from_cluster(self, v, load=False):
    """
    Setter method for nodes_disconnected_from_cluster, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/nodes_disconnected_from_cluster (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_nodes_disconnected_from_cluster is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_nodes_disconnected_from_cluster() directly.

    YANG Description: Number of nodes disconnected from cluster
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="nodes-disconnected-from-cluster", rest_name="nodes-disconnected-from-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """nodes_disconnected_from_cluster must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="nodes-disconnected-from-cluster", rest_name="nodes-disconnected-from-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)""",
        })

    self.__nodes_disconnected_from_cluster = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_nodes_disconnected_from_cluster(self):
    self.__nodes_disconnected_from_cluster = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="nodes-disconnected-from-cluster", rest_name="nodes-disconnected-from-cluster", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='uint16', is_config=True)


  def _get_cluster_nodes(self):
    """
    Getter method for cluster_nodes, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/cluster_nodes (container)
    """
    return self.__cluster_nodes
      
  def _set_cluster_nodes(self, v, load=False):
    """
    Setter method for cluster_nodes, mapped from YANG variable /brocade_cluster_rpc/show_cluster_management/output/cluster_nodes (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_cluster_nodes is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_cluster_nodes() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=cluster_nodes.cluster_nodes, is_container='container', presence=False, yang_name="cluster-nodes", rest_name="cluster-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """cluster_nodes must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=cluster_nodes.cluster_nodes, is_container='container', presence=False, yang_name="cluster-nodes", rest_name="cluster-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='container', is_config=True)""",
        })

    self.__cluster_nodes = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_cluster_nodes(self):
    self.__cluster_nodes = YANGDynClass(base=cluster_nodes.cluster_nodes, is_container='container', presence=False, yang_name="cluster-nodes", rest_name="cluster-nodes", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='http://brocade.com/ns/brocade-cluster', defining_module='brocade-cluster', yang_type='container', is_config=True)

  principal_switch_mac = __builtin__.property(_get_principal_switch_mac, _set_principal_switch_mac)
  total_nodes_in_cluster = __builtin__.property(_get_total_nodes_in_cluster, _set_total_nodes_in_cluster)
  nodes_disconnected_from_cluster = __builtin__.property(_get_nodes_disconnected_from_cluster, _set_nodes_disconnected_from_cluster)
  cluster_nodes = __builtin__.property(_get_cluster_nodes, _set_cluster_nodes)


  _pyangbind_elements = {'principal_switch_mac': principal_switch_mac, 'total_nodes_in_cluster': total_nodes_in_cluster, 'nodes_disconnected_from_cluster': nodes_disconnected_from_cluster, 'cluster_nodes': cluster_nodes, }


