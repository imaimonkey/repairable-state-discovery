# V2R cluster inventory

2026-09-25T04:51:33.755961+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318907441152 available bytes; 82.21% used; 112480344 free inodes.

server1 `/home`: 318907441152 available bytes; 82.21% used; 112480344 free inodes.

server1 `/tmp`: 318907441152 available bytes; 82.21% used; 112480344 free inodes.

server1 `/var/tmp`: 318907441152 available bytes; 82.21% used; 112480344 free inodes.

server1 `/mnt/raid5`: 408672690176 available bytes; 98.13% used; 337589074 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22940467200 available bytes; 98.72% used; 110410440 free inodes.

server2 `/home`: 22940467200 available bytes; 98.72% used; 110410440 free inodes.

server2 `/tmp`: 22940467200 available bytes; 98.72% used; 110410440 free inodes.

server2 `/var/tmp`: 22940467200 available bytes; 98.72% used; 110410440 free inodes.

server2 `/mnt/raid5`: 462368432128 available bytes; 96.81% used; 445109138 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84339068928 available bytes; 95.29% used; 114156076 free inodes.

server3 `/home`: 84339068928 available bytes; 95.29% used; 114156076 free inodes.

server3 `/data`: 143108198400 available bytes; 98.02% used; 225815720 free inodes.

server3 `/tmp`: 84339068928 available bytes; 95.29% used; 114156076 free inodes.

server3 `/var/tmp`: 84339068928 available bytes; 95.29% used; 114156076 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105661661184 available bytes; 94.10% used; 114350496 free inodes.

server4 `/home`: 105661661184 available bytes; 94.10% used; 114350496 free inodes.

server4 `/data`: 27946602496 available bytes; 99.61% used; 224961725 free inodes.

server4 `/tmp`: 105661661184 available bytes; 94.10% used; 114350496 free inodes.

server4 `/var/tmp`: 105661661184 available bytes; 94.10% used; 114350496 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
