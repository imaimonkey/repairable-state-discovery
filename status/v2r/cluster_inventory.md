# V2R cluster inventory

2026-09-25T08:19:09.658788+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318827642880 available bytes; 82.21% used; 112480351 free inodes.

server1 `/home`: 318827642880 available bytes; 82.21% used; 112480351 free inodes.

server1 `/tmp`: 318827642880 available bytes; 82.21% used; 112480351 free inodes.

server1 `/var/tmp`: 318827642880 available bytes; 82.21% used; 112480351 free inodes.

server1 `/mnt/raid5`: 376296615936 available bytes; 98.27% used; 337557415 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22834094080 available bytes; 98.73% used; 110410480 free inodes.

server2 `/home`: 22834094080 available bytes; 98.73% used; 110410480 free inodes.

server2 `/tmp`: 22834094080 available bytes; 98.73% used; 110410480 free inodes.

server2 `/var/tmp`: 22834094080 available bytes; 98.73% used; 110410480 free inodes.

server2 `/mnt/raid5`: 333625040896 available bytes; 97.69% used; 445094807 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84439236608 available bytes; 95.29% used; 114156053 free inodes.

server3 `/home`: 84439236608 available bytes; 95.29% used; 114156053 free inodes.

server3 `/data`: 142385274880 available bytes; 98.03% used; 225811875 free inodes.

server3 `/tmp`: 84439236608 available bytes; 95.29% used; 114156053 free inodes.

server3 `/var/tmp`: 84439236608 available bytes; 95.29% used; 114156053 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105624977408 available bytes; 94.11% used; 114350334 free inodes.

server4 `/home`: 105624977408 available bytes; 94.11% used; 114350334 free inodes.

server4 `/data`: 247976251392 available bytes; 96.57% used; 225006688 free inodes.

server4 `/tmp`: 105624977408 available bytes; 94.11% used; 114350334 free inodes.

server4 `/var/tmp`: 105624977408 available bytes; 94.11% used; 114350334 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
