# V2R cluster inventory

2026-09-25T20:07:11.789113+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318717296640 available bytes; 82.22% used; 112476348 free inodes.

server1 `/home`: 318717296640 available bytes; 82.22% used; 112476348 free inodes.

server1 `/tmp`: 318717296640 available bytes; 82.22% used; 112476348 free inodes.

server1 `/var/tmp`: 318717296640 available bytes; 82.22% used; 112476348 free inodes.

server1 `/mnt/raid5`: 370799878144 available bytes; 98.30% used; 337540614 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23095554048 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311054618624 available bytes; 97.85% used; 445063443 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84383010816 available bytes; 95.29% used; 114152624 free inodes.

server3 `/home`: 84383010816 available bytes; 95.29% used; 114152624 free inodes.

server3 `/data`: 127194169344 available bytes; 98.24% used; 225808420 free inodes.

server3 `/tmp`: 84383010816 available bytes; 95.29% used; 114152624 free inodes.

server3 `/var/tmp`: 84383010816 available bytes; 95.29% used; 114152624 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105673605120 available bytes; 94.10% used; 114349572 free inodes.

server4 `/home`: 105673605120 available bytes; 94.10% used; 114349572 free inodes.

server4 `/data`: 229427068928 available bytes; 96.83% used; 224929207 free inodes.

server4 `/tmp`: 105673605120 available bytes; 94.10% used; 114349572 free inodes.

server4 `/var/tmp`: 105673605120 available bytes; 94.10% used; 114349572 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
