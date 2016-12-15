
from operator import attrgetter
import pyangbind.lib.xpathhelper as xpathhelper
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType, RestrictedClassType, TypedListType
from pyangbind.lib.yangtypes import YANGBool, YANGListType, YANGDynClass, ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import __builtin__
import bundle_message
class interface_refresh_reduction(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module brocade-mpls - based on the path /mpls-config/router/mpls/mpls-cmds-holder/mpls-interface/rsvp/interface-refresh-reduction. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_rest_name', '_extmethods', '__refresh_reduction_all','__summary_refresh','__bundle_message','__rsvp_refresh_reduction_disable',)

  _yang_name = 'interface-refresh-reduction'
  _rest_name = 'refresh-reduction'

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
    self.__refresh_reduction_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="refresh-reduction-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'All Refresh reduction functionalities', u'hidden': u'full', u'cli-full-no': None, u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__summary_refresh = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-refresh", rest_name="summary-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Refresh Reduction Summary Refresh feature', u'cli-full-no': None, u'alt-name': u'summary-refresh'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    self.__bundle_message = YANGDynClass(base=bundle_message.bundle_message, is_container='container', yang_name="bundle-message", rest_name="bundle-message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh Reduction bundle messaging feature', u'alt-name': u'bundle-message'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    self.__rsvp_refresh_reduction_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-refresh-reduction-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable RSVP Refresh reduction on this interface', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

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
      return [u'mpls-config', u'router', u'mpls', u'mpls-cmds-holder', u'mpls-interface', u'rsvp', u'interface-refresh-reduction']

  def _rest_path(self):
    if hasattr(self, "_parent"):
      if self._rest_name:
        return self._parent._rest_path()+[self._rest_name]
      else:
        return self._parent._rest_path()
    else:
      return [u'router', u'mpls', u'mpls-interface', u'rsvp', u'refresh-reduction']

  def _get_refresh_reduction_all(self):
    """
    Getter method for refresh_reduction_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/refresh_reduction_all (empty)
    """
    return self.__refresh_reduction_all
      
  def _set_refresh_reduction_all(self, v, load=False):
    """
    Setter method for refresh_reduction_all, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/refresh_reduction_all (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_refresh_reduction_all is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_refresh_reduction_all() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="refresh-reduction-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'All Refresh reduction functionalities', u'hidden': u'full', u'cli-full-no': None, u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """refresh_reduction_all must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="refresh-reduction-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'All Refresh reduction functionalities', u'hidden': u'full', u'cli-full-no': None, u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__refresh_reduction_all = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_refresh_reduction_all(self):
    self.__refresh_reduction_all = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="refresh-reduction-all", rest_name="all", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'All Refresh reduction functionalities', u'hidden': u'full', u'cli-full-no': None, u'alt-name': u'all'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_summary_refresh(self):
    """
    Getter method for summary_refresh, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/summary_refresh (empty)
    """
    return self.__summary_refresh
      
  def _set_summary_refresh(self, v, load=False):
    """
    Setter method for summary_refresh, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/summary_refresh (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_summary_refresh is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_summary_refresh() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="summary-refresh", rest_name="summary-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Refresh Reduction Summary Refresh feature', u'cli-full-no': None, u'alt-name': u'summary-refresh'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """summary_refresh must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-refresh", rest_name="summary-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Refresh Reduction Summary Refresh feature', u'cli-full-no': None, u'alt-name': u'summary-refresh'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__summary_refresh = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_summary_refresh(self):
    self.__summary_refresh = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="summary-refresh", rest_name="summary-refresh", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'cli-full-command': None, u'info': u'Refresh Reduction Summary Refresh feature', u'cli-full-no': None, u'alt-name': u'summary-refresh'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)


  def _get_bundle_message(self):
    """
    Getter method for bundle_message, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/bundle_message (container)
    """
    return self.__bundle_message
      
  def _set_bundle_message(self, v, load=False):
    """
    Setter method for bundle_message, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/bundle_message (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_bundle_message is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_bundle_message() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=bundle_message.bundle_message, is_container='container', yang_name="bundle-message", rest_name="bundle-message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh Reduction bundle messaging feature', u'alt-name': u'bundle-message'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """bundle_message must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=bundle_message.bundle_message, is_container='container', yang_name="bundle-message", rest_name="bundle-message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh Reduction bundle messaging feature', u'alt-name': u'bundle-message'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)""",
        })

    self.__bundle_message = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_bundle_message(self):
    self.__bundle_message = YANGDynClass(base=bundle_message.bundle_message, is_container='container', yang_name="bundle-message", rest_name="bundle-message", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Refresh Reduction bundle messaging feature', u'alt-name': u'bundle-message'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='container', is_config=True)


  def _get_rsvp_refresh_reduction_disable(self):
    """
    Getter method for rsvp_refresh_reduction_disable, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/rsvp_refresh_reduction_disable (empty)
    """
    return self.__rsvp_refresh_reduction_disable
      
  def _set_rsvp_refresh_reduction_disable(self, v, load=False):
    """
    Setter method for rsvp_refresh_reduction_disable, mapped from YANG variable /mpls_config/router/mpls/mpls_cmds_holder/mpls_interface/rsvp/interface_refresh_reduction/rsvp_refresh_reduction_disable (empty)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_rsvp_refresh_reduction_disable is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_rsvp_refresh_reduction_disable() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=YANGBool, is_leaf=True, yang_name="rsvp-refresh-reduction-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable RSVP Refresh reduction on this interface', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """rsvp_refresh_reduction_disable must be of a type compatible with empty""",
          'defined-type': "empty",
          'generated-type': """YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-refresh-reduction-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable RSVP Refresh reduction on this interface', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)""",
        })

    self.__rsvp_refresh_reduction_disable = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_rsvp_refresh_reduction_disable(self):
    self.__rsvp_refresh_reduction_disable = YANGDynClass(base=YANGBool, is_leaf=True, yang_name="rsvp-refresh-reduction-disable", rest_name="disable", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions={u'tailf-common': {u'info': u'Disable RSVP Refresh reduction on this interface', u'alt-name': u'disable'}}, namespace='urn:brocade.com:mgmt:brocade-mpls', defining_module='brocade-mpls', yang_type='empty', is_config=True)

  refresh_reduction_all = __builtin__.property(_get_refresh_reduction_all, _set_refresh_reduction_all)
  summary_refresh = __builtin__.property(_get_summary_refresh, _set_summary_refresh)
  bundle_message = __builtin__.property(_get_bundle_message, _set_bundle_message)
  rsvp_refresh_reduction_disable = __builtin__.property(_get_rsvp_refresh_reduction_disable, _set_rsvp_refresh_reduction_disable)


  _pyangbind_elements = {'refresh_reduction_all': refresh_reduction_all, 'summary_refresh': summary_refresh, 'bundle_message': bundle_message, 'rsvp_refresh_reduction_disable': rsvp_refresh_reduction_disable, }


