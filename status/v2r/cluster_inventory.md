# V2R cluster inventory

2026-09-25T11:18:11.434354+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319062134784 available bytes; 82.20% used; 112478863 free inodes.

server1 `/home`: 319062134784 available bytes; 82.20% used; 112478863 free inodes.

server1 `/tmp`: 319062134784 available bytes; 82.20% used; 112478863 free inodes.

server1 `/var/tmp`: 319062134784 available bytes; 82.20% used; 112478863 free inodes.

server1 `/mnt/raid5`: 364169617408 available bytes; 98.33% used; 337550310 free inodes.
| server2 | True | ['1', '2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 22906245120 available bytes; 98.72% used; 110409986 free inodes.

server2 `/home`: 22906245120 available bytes; 98.72% used; 110409986 free inodes.

server2 `/tmp`: 22906245120 available bytes; 98.72% used; 110409986 free inodes.

server2 `/var/tmp`: 22906245120 available bytes; 98.72% used; 110409986 free inodes.

server2 `/mnt/raid5`: 327905067008 available bytes; 97.73% used; 445084123 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84141383680 available bytes; 95.30% used; 114155498 free inodes.

server3 `/home`: 84141383680 available bytes; 95.30% used; 114155498 free inodes.

server3 `/data`: 142085885952 available bytes; 98.04% used; 225814392 free inodes.

server3 `/tmp`: 84141383680 available bytes; 95.30% used; 114155498 free inodes.

server3 `/var/tmp`: 84141383680 available bytes; 95.30% used; 114155498 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105611948032 available bytes; 94.11% used; 114350251 free inodes.

server4 `/home`: 105611948032 available bytes; 94.11% used; 114350251 free inodes.

server4 `/data`: 238633803776 available bytes; 96.70% used; 224981522 free inodes.

server4 `/tmp`: 105611948032 available bytes; 94.11% used; 114350251 free inodes.

server4 `/var/tmp`: 105611948032 available bytes; 94.11% used; 114350251 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
