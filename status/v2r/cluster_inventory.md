# V2R cluster inventory

2026-09-24T10:50:00.957784+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324388073472 available bytes; 81.90% used; 112489111 free inodes.

server1 `/home`: 324388073472 available bytes; 81.90% used; 112489111 free inodes.

server1 `/tmp`: 324388073472 available bytes; 81.90% used; 112489111 free inodes.

server1 `/var/tmp`: 324388073472 available bytes; 81.90% used; 112489111 free inodes.

server1 `/mnt/raid5`: 499757748224 available bytes; 97.71% used; 337695450 free inodes.
| server2 | True | ['5'] | [] |

server2 `/`: 57711710208 available bytes; 96.78% used; 110430405 free inodes.

server2 `/home`: 57711710208 available bytes; 96.78% used; 110430405 free inodes.

server2 `/tmp`: 57711710208 available bytes; 96.78% used; 110430405 free inodes.

server2 `/var/tmp`: 57711710208 available bytes; 96.78% used; 110430405 free inodes.

server2 `/mnt/raid5`: 512180822016 available bytes; 96.46% used; 445174701 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85799223296 available bytes; 95.21% used; 114198175 free inodes.

server3 `/home`: 85799223296 available bytes; 95.21% used; 114198175 free inodes.

server3 `/data`: 164096098304 available bytes; 97.73% used; 225817830 free inodes.

server3 `/tmp`: 85799223296 available bytes; 95.21% used; 114198175 free inodes.

server3 `/var/tmp`: 85799223296 available bytes; 95.21% used; 114198175 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105735372800 available bytes; 94.10% used; 114348954 free inodes.

server4 `/home`: 105735372800 available bytes; 94.10% used; 114348954 free inodes.

server4 `/data`: 132794728448 available bytes; 98.16% used; 225258313 free inodes.

server4 `/tmp`: 105735372800 available bytes; 94.10% used; 114348954 free inodes.

server4 `/var/tmp`: 105735372800 available bytes; 94.10% used; 114348954 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
