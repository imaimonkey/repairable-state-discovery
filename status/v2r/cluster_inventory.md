# V2R cluster inventory

2026-09-25T10:04:12.121736+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318835355648 available bytes; 82.21% used; 112480376 free inodes.

server1 `/home`: 318835355648 available bytes; 82.21% used; 112480376 free inodes.

server1 `/tmp`: 318835355648 available bytes; 82.21% used; 112480376 free inodes.

server1 `/var/tmp`: 318835355648 available bytes; 82.21% used; 112480376 free inodes.

server1 `/mnt/raid5`: 364731002880 available bytes; 98.33% used; 337556980 free inodes.
| server2 | True | ['6'] | [] |

server2 `/`: 22826889216 available bytes; 98.73% used; 110410468 free inodes.

server2 `/home`: 22826889216 available bytes; 98.73% used; 110410468 free inodes.

server2 `/tmp`: 22826889216 available bytes; 98.73% used; 110410468 free inodes.

server2 `/var/tmp`: 22826889216 available bytes; 98.73% used; 110410468 free inodes.

server2 `/mnt/raid5`: 316922281984 available bytes; 97.81% used; 445091241 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84418629632 available bytes; 95.29% used; 114156039 free inodes.

server3 `/home`: 84418629632 available bytes; 95.29% used; 114156039 free inodes.

server3 `/data`: 141879373824 available bytes; 98.04% used; 225810029 free inodes.

server3 `/tmp`: 84418629632 available bytes; 95.29% used; 114156039 free inodes.

server3 `/var/tmp`: 84418629632 available bytes; 95.29% used; 114156039 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105614274560 available bytes; 94.11% used; 114350276 free inodes.

server4 `/home`: 105614274560 available bytes; 94.11% used; 114350276 free inodes.

server4 `/data`: 240013148160 available bytes; 96.68% used; 224991197 free inodes.

server4 `/tmp`: 105614274560 available bytes; 94.11% used; 114350276 free inodes.

server4 `/var/tmp`: 105614274560 available bytes; 94.11% used; 114350276 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
