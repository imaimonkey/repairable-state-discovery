# V2R cluster inventory

2026-09-25T08:14:34.079486+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318839246848 available bytes; 82.21% used; 112480352 free inodes.

server1 `/home`: 318839246848 available bytes; 82.21% used; 112480352 free inodes.

server1 `/tmp`: 318839246848 available bytes; 82.21% used; 112480352 free inodes.

server1 `/var/tmp`: 318839246848 available bytes; 82.21% used; 112480352 free inodes.

server1 `/mnt/raid5`: 379188944896 available bytes; 98.26% used; 337557576 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22836412416 available bytes; 98.73% used; 110410481 free inodes.

server2 `/home`: 22836412416 available bytes; 98.73% used; 110410481 free inodes.

server2 `/tmp`: 22836412416 available bytes; 98.73% used; 110410481 free inodes.

server2 `/var/tmp`: 22836412416 available bytes; 98.73% used; 110410481 free inodes.

server2 `/mnt/raid5`: 333767626752 available bytes; 97.69% used; 445095095 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84436275200 available bytes; 95.29% used; 114156051 free inodes.

server3 `/home`: 84436275200 available bytes; 95.29% used; 114156051 free inodes.

server3 `/data`: 142384607232 available bytes; 98.03% used; 225811946 free inodes.

server3 `/tmp`: 84436275200 available bytes; 95.29% used; 114156051 free inodes.

server3 `/var/tmp`: 84436275200 available bytes; 95.29% used; 114156051 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105625092096 available bytes; 94.11% used; 114350335 free inodes.

server4 `/home`: 105625092096 available bytes; 94.11% used; 114350335 free inodes.

server4 `/data`: 249003118592 available bytes; 96.56% used; 225007692 free inodes.

server4 `/tmp`: 105625092096 available bytes; 94.11% used; 114350335 free inodes.

server4 `/var/tmp`: 105625092096 available bytes; 94.11% used; 114350335 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
