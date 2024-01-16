from pot.oci.serialization import Engine

from pot.oci.serialization.container import DockerContainerAdapter, PodmanContainerAdapter
from pot.oci.serialization.image import DockerImageAdapter, PodmanImageAdapter


class DockerSerializationEngine(Engine):
    def __init__(self, entrypoint: str):
        super().__init__(entrypoint, DockerImageAdapter(), DockerContainerAdapter())


class PodmanSerializationEngine(Engine):
    def __init__(self, entrypoint: str):
        super().__init__(entrypoint, PodmanImageAdapter(), PodmanContainerAdapter()))