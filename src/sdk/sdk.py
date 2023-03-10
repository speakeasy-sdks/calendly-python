__doc__ = """ SDK Documentation: Calendly’s API is [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer)-based and has predictable resource-oriented URLs. It uses **JSON** for request and response bodies and standard HTTP methods, authentication, and response codes.<br>

##### Authenticate with personal access tokens or OAuth 2.0

To access Calendly data through the API, you can authenticate with **personal access tokens** or **OAuth 2.0**. To learn more about these authentication methods and when and how to use them, see [Getting Started with the Calendly API](https://developer.calendly.com/getting-started)."""
import requests as requests_http
from . import utils
from .activity_log import ActivityLog
from .availability import Availability
from .data_compliance import DataCompliance
from .event_types import EventTypes
from .organizations import Organizations
from .routing_forms import RoutingForms
from .scheduled_events import ScheduledEvents
from .scheduling_links import SchedulingLinks
from .shares import Shares
from .users import Users
from .webhooks import Webhooks
from sdk.models import shared

SERVERS = [
	"https://api.calendly.com",
]

class SDK:
    r"""SDK Documentation: Calendly’s API is [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer)-based and has predictable resource-oriented URLs. It uses **JSON** for request and response bodies and standard HTTP methods, authentication, and response codes.<br>
    
    ##### Authenticate with personal access tokens or OAuth 2.0
    
    To access Calendly data through the API, you can authenticate with **personal access tokens** or **OAuth 2.0**. To learn more about these authentication methods and when and how to use them, see [Getting Started with the Calendly API](https://developer.calendly.com/getting-started)."""
    activity_log: ActivityLog
    availability: Availability
    data_compliance: DataCompliance
    event_types: EventTypes
    organizations: Organizations
    routing_forms: RoutingForms
    scheduled_events: ScheduledEvents
    scheduling_links: SchedulingLinks
    shares: Shares
    users: Users
    webhooks: Webhooks
    
    _client: requests_http.Session
    _security_client: requests_http.Session
    _security: shared.Security
    _server_url: str = SERVERS[0]
    _language: str = "python"
    _sdk_version: str = "0.1.0"
    _gen_version: str = "1.9.1"

    def __init__(self) -> None:
        self._client = requests_http.Session()
        self._security_client = requests_http.Session()
        self._init_sdks()

    def config_server_url(self, server_url: str, params: dict[str, str] = None):
        if params is not None:
            self._server_url = utils.template_url(server_url, params)
        else:
            self._server_url = server_url

        self._init_sdks()
    
    

    def config_client(self, client: requests_http.Session):
        self._client = client
        
        if self._security is not None:
            self._security_client = utils.configure_security_client(self._client, self._security)
        self._init_sdks()
    
    def config_security(self, security: shared.Security):
        self._security = security
        self._security_client = utils.configure_security_client(self._client, security)
        self._init_sdks()
    
    def _init_sdks(self):
        self.activity_log = ActivityLog(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.availability = Availability(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.data_compliance = DataCompliance(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.event_types = EventTypes(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.organizations = Organizations(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.routing_forms = RoutingForms(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.scheduled_events = ScheduledEvents(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.scheduling_links = SchedulingLinks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.shares = Shares(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.users = Users(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
        self.webhooks = Webhooks(
            self._client,
            self._security_client,
            self._server_url,
            self._language,
            self._sdk_version,
            self._gen_version
        )
        
    