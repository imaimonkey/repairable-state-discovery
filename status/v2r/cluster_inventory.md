# V2R cluster inventory

2026-09-25T07:33:42.998136+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 318870872064 available bytes; 82.21% used; 112480374 free inodes.

server1 `/home`: 318870872064 available bytes; 82.21% used; 112480374 free inodes.

server1 `/tmp`: 318870872064 available bytes; 82.21% used; 112480374 free inodes.

server1 `/var/tmp`: 318870872064 available bytes; 82.21% used; 112480374 free inodes.

server1 `/mnt/raid5`: 385876951040 available bytes; 98.23% used; 337558399 free inodes.
| server2 | True | [] | [] |

server2 `/`: 22859214848 available bytes; 98.72% used; 110410496 free inodes.

server2 `/home`: 22859214848 available bytes; 98.72% used; 110410496 free inodes.

server2 `/tmp`: 22859214848 available bytes; 98.72% used; 110410496 free inodes.

server2 `/var/tmp`: 22859214848 available bytes; 98.72% used; 110410496 free inodes.

server2 `/mnt/raid5`: 342337798144 available bytes; 97.63% used; 445097080 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84436774912 available bytes; 95.29% used; 114156035 free inodes.

server3 `/home`: 84436774912 available bytes; 95.29% used; 114156035 free inodes.

server3 `/data`: 142398558208 available bytes; 98.03% used; 225812650 free inodes.

server3 `/tmp`: 84436774912 available bytes; 95.29% used; 114156035 free inodes.

server3 `/var/tmp`: 84436774912 available bytes; 95.29% used; 114156035 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105637740544 available bytes; 94.11% used; 114350352 free inodes.

server4 `/home`: 105637740544 available bytes; 94.11% used; 114350352 free inodes.

server4 `/data`: 249086119936 available bytes; 96.56% used; 225013819 free inodes.

server4 `/tmp`: 105637740544 available bytes; 94.11% used; 114350352 free inodes.

server4 `/var/tmp`: 105637740544 available bytes; 94.11% used; 114350352 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
