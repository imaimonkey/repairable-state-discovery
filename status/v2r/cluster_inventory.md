# V2R cluster inventory

2026-09-24T09:33:55.165257+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 324455546880 available bytes; 81.90% used; 112489829 free inodes.

server1 `/home`: 324455546880 available bytes; 81.90% used; 112489829 free inodes.

server1 `/tmp`: 324455546880 available bytes; 81.90% used; 112489829 free inodes.

server1 `/var/tmp`: 324455546880 available bytes; 81.90% used; 112489829 free inodes.

server1 `/mnt/raid5`: 502492971008 available bytes; 97.69% used; 337712921 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57766412288 available bytes; 96.78% used; 110430802 free inodes.

server2 `/home`: 57766412288 available bytes; 96.78% used; 110430802 free inodes.

server2 `/tmp`: 57766412288 available bytes; 96.78% used; 110430802 free inodes.

server2 `/var/tmp`: 57766412288 available bytes; 96.78% used; 110430802 free inodes.

server2 `/mnt/raid5`: 514486300672 available bytes; 96.45% used; 445177669 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85354967040 available bytes; 95.24% used; 114170909 free inodes.

server3 `/home`: 85354967040 available bytes; 95.24% used; 114170909 free inodes.

server3 `/data`: 165769166848 available bytes; 97.71% used; 225820466 free inodes.

server3 `/tmp`: 85354967040 available bytes; 95.24% used; 114170909 free inodes.

server3 `/var/tmp`: 85354967040 available bytes; 95.24% used; 114170909 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105757609984 available bytes; 94.10% used; 114349047 free inodes.

server4 `/home`: 105757609984 available bytes; 94.10% used; 114349047 free inodes.

server4 `/data`: 154581180416 available bytes; 97.86% used; 225273241 free inodes.

server4 `/tmp`: 105757609984 available bytes; 94.10% used; 114349047 free inodes.

server4 `/var/tmp`: 105757609984 available bytes; 94.10% used; 114349047 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
