
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
class prefixlist(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-rbridge - based on the path /rbridge-id/router/router-bgp/address-family/ipv4/ipv4-unicast/default-vrf/neighbor/af-ipv4-neighbor-peergroup-holder/af-ipv4-neighbor-peergroup/af-neighbor-capability/orf/prefixlist. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__prefixlist_status','__prefixlist_send','__prefixlist_receive',)

  _yang_name = 'prefixlist'
  _rest_name = 'prefixlist'

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
    self.__prefixlist_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../prefixlist-send?$(../prefixlist-receive?neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist\n:\\r):\\r):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__prefixlist_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-send?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist receive\n):\\r)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    self.__prefixlist_send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-receive?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist send\n):\\r)', u'alt-name': u'send', u'info': u'Capability to SEND the ORF to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

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
      return [u'rbridge-id', u'router', u'router-bgp', u'address-family', u'ipv4', u'ipv4-unicast', u'default-vrf', u'neighbor', u'af-ipv4-neighbor-peergroup-holder', u'af-ipv4-neighbor-peergroup', u'af-neighbor-capability', u'orf', u'prefixlist']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'rbridge-id', u'router', u'bgp', u'address-family', u'ipv4', u'unicast', u'neighbor', u'capability', u'orf', u'prefixlist']

  def _get_prefixlist_status(self):
    """
    Getter method for prefixlist_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_status (empty)

    YANG Description: This element will be set if either(or both) send,receive options are configured
    """
    return self.__prefixlist_status
      
  def _set_prefixlist_status(self, v, load=False):
    """
    Setter method for prefixlist_status, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_status (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefixlist_status is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefixlist_status() directly.

    YANG Description: This element will be set if either(or both) send,receive options are configured
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="prefixlist-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../prefixlist-send?$(../prefixlist-receive?neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist\n:\\r):\\r):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefixlist_status must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../prefixlist-send?$(../prefixlist-receive?neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist\n:\\r):\\r):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__prefixlist_status = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefixlist_status(self):
    self.__prefixlist_status = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-status", rest_name="", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-run-template': u'$(.?$(../prefixlist-send?$(../prefixlist-receive?neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist\n:\\r):\\r):\\r)', u'cli-drop-node-name': None}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_prefixlist_send(self):
    """
    Getter method for prefixlist_send, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_send (empty)

    YANG Description: Capability to SEND the ORF to this neighbor
    """
    return self.__prefixlist_send
      
  def _set_prefixlist_send(self, v, load=False):
    """
    Setter method for prefixlist_send, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_send (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefixlist_send is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefixlist_send() directly.

    YANG Description: Capability to SEND the ORF to this neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="prefixlist-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-receive?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist send\n):\\r)', u'alt-name': u'send', u'info': u'Capability to SEND the ORF to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefixlist_send must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-receive?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist send\n):\\r)', u'alt-name': u'send', u'info': u'Capability to SEND the ORF to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__prefixlist_send = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefixlist_send(self):
    self.__prefixlist_send = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-send", rest_name="send", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-receive?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist send\n):\\r)', u'alt-name': u'send', u'info': u'Capability to SEND the ORF to this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)


  def _get_prefixlist_receive(self):
    """
    Getter method for prefixlist_receive, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_receive (empty)

    YANG Description: Capability to RECEIVE the ORF from this neighbor
    """
    return self.__prefixlist_receive
      
  def _set_prefixlist_receive(self, v, load=False):
    """
    Setter method for prefixlist_receive, mapped from YANG variable /rbridge_id/router/router_bgp/address_family/ipv4/ipv4_unicast/default_vrf/neighbor/af_ipv4_neighbor_peergroup_holder/af_ipv4_neighbor_peergroup/af_neighbor_capability/orf/prefixlist/prefixlist_receive (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_prefixlist_receive is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_prefixlist_receive() directly.

    YANG Description: Capability to RECEIVE the ORF from this neighbor
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="prefixlist-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-send?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist receive\n):\\r)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """prefixlist_receive must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-send?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist receive\n):\\r)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)""",
        })

    self.__prefixlist_receive = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_prefixlist_receive(self):
    self.__prefixlist_receive = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="prefixlist-receive", rest_name="receive", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'cli-run-template': u'$(.?$(../prefixlist-send?\\r:neighbor $(../../../../af-ipv4-neighbor-peergroup-name) capability orf prefixlist receive\n):\\r)', u'alt-name': u'receive', u'info': u'Capability to RECEIVE the ORF from this neighbor'}}, namespace='urn:brocade.com:mgmt:brocade-bgp', defining_module='brocade-bgp', yang_type='empty', is_config=True)

  prefixlist_status = __builtin__.property(_get_prefixlist_status, _set_prefixlist_status)
  prefixlist_send = __builtin__.property(_get_prefixlist_send, _set_prefixlist_send)
  prefixlist_receive = __builtin__.property(_get_prefixlist_receive, _set_prefixlist_receive)


  _pyangbind_elements = {'prefixlist_status': prefixlist_status, 'prefixlist_send': prefixlist_send, 'prefixlist_receive': prefixlist_receive, }


