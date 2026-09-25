# V2R cluster inventory

2026-09-25T05:20:47.715033+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318877802496 available bytes; 82.21% used; 112480258 free inodes.

server1 `/home`: 318877802496 available bytes; 82.21% used; 112480258 free inodes.

server1 `/tmp`: 318877802496 available bytes; 82.21% used; 112480258 free inodes.

server1 `/var/tmp`: 318877802496 available bytes; 82.21% used; 112480258 free inodes.

server1 `/mnt/raid5`: 408529285120 available bytes; 98.13% used; 337569419 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22929965056 available bytes; 98.72% used; 110410443 free inodes.

server2 `/home`: 22929965056 available bytes; 98.72% used; 110410443 free inodes.

server2 `/tmp`: 22929965056 available bytes; 98.72% used; 110410443 free inodes.

server2 `/var/tmp`: 22929965056 available bytes; 98.72% used; 110410443 free inodes.

server2 `/mnt/raid5`: 461462806528 available bytes; 96.81% used; 445108501 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84338012160 available bytes; 95.29% used; 114156044 free inodes.

server3 `/home`: 84338012160 available bytes; 95.29% used; 114156044 free inodes.

server3 `/data`: 142778204160 available bytes; 98.03% used; 225815006 free inodes.

server3 `/tmp`: 84338012160 available bytes; 95.29% used; 114156044 free inodes.

server3 `/var/tmp`: 84338012160 available bytes; 95.29% used; 114156044 free inodes.
| server4 | True | ['6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105658720256 available bytes; 94.10% used; 114350403 free inodes.

server4 `/home`: 105658720256 available bytes; 94.10% used; 114350403 free inodes.

server4 `/data`: 26288418816 available bytes; 99.64% used; 224959869 free inodes.

server4 `/tmp`: 105658720256 available bytes; 94.10% used; 114350403 free inodes.

server4 `/var/tmp`: 105658720256 available bytes; 94.10% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
