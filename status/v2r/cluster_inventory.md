# V2R cluster inventory

2026-09-23T23:14:45.133651+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['6', '7'] | ['/tmp', '/var/tmp', '/mnt/raid5'] | reference_compatible=False |

server1 `/`: 325665996800 available bytes; 81.83% used; 112501618 free inodes.

server1 `/home`: 325665996800 available bytes; 81.83% used; 112501618 free inodes.

server1 `/tmp`: 325665996800 available bytes; 81.83% used; 112501618 free inodes.

server1 `/var/tmp`: 325665996800 available bytes; 81.83% used; 112501618 free inodes.

server1 `/mnt/raid5`: 1387934343168 available bytes; 93.63% used; 337739865 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 41053032448 available bytes; 97.71% used; 110432609 free inodes.

server2 `/home`: 41053032448 available bytes; 97.71% used; 110432609 free inodes.

server2 `/tmp`: 41053032448 available bytes; 97.71% used; 110432609 free inodes.

server2 `/var/tmp`: 41053032448 available bytes; 97.71% used; 110432609 free inodes.

server2 `/mnt/raid5`: 534967365632 available bytes; 96.30% used; 445206083 free inodes.
| server3 | True | ['3'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292247457792 available bytes; 83.69% used; 114171237 free inodes.

server3 `/home`: 292247457792 available bytes; 83.69% used; 114171237 free inodes.

server3 `/data`: 82328940544 available bytes; 98.86% used; 225846053 free inodes.

server3 `/tmp`: 292247457792 available bytes; 83.69% used; 114171237 free inodes.

server3 `/var/tmp`: 292247457792 available bytes; 83.69% used; 114171237 free inodes.
| server4 | True | ['3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106263646208 available bytes; 94.07% used; 114352915 free inodes.

server4 `/home`: 106263646208 available bytes; 94.07% used; 114352915 free inodes.

server4 `/data`: 298363514880 available bytes; 95.88% used; 225428922 free inodes.

server4 `/tmp`: 106263646208 available bytes; 94.07% used; 114352915 free inodes.

server4 `/var/tmp`: 106263646208 available bytes; 94.07% used; 114352915 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
