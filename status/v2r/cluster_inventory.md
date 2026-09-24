# V2R cluster inventory

2026-09-24T10:01:52.999588+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324428660736 available bytes; 81.90% used; 112489511 free inodes.

server1 `/home`: 324428660736 available bytes; 81.90% used; 112489511 free inodes.

server1 `/tmp`: 324428660736 available bytes; 81.90% used; 112489511 free inodes.

server1 `/var/tmp`: 324428660736 available bytes; 81.90% used; 112489511 free inodes.

server1 `/mnt/raid5`: 500699230208 available bytes; 97.70% used; 337701157 free inodes.
| server2 | True | [] | [] |

server2 `/`: 57750470656 available bytes; 96.78% used; 110430736 free inodes.

server2 `/home`: 57750470656 available bytes; 96.78% used; 110430736 free inodes.

server2 `/tmp`: 57750470656 available bytes; 96.78% used; 110430736 free inodes.

server2 `/var/tmp`: 57750470656 available bytes; 96.78% used; 110430736 free inodes.

server2 `/mnt/raid5`: 513612840960 available bytes; 96.45% used; 445176802 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85384556544 available bytes; 95.24% used; 114173574 free inodes.

server3 `/home`: 85384556544 available bytes; 95.24% used; 114173574 free inodes.

server3 `/data`: 164490874880 available bytes; 97.73% used; 225819239 free inodes.

server3 `/tmp`: 85384556544 available bytes; 95.24% used; 114173574 free inodes.

server3 `/var/tmp`: 85384556544 available bytes; 95.24% used; 114173574 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105747968000 available bytes; 94.10% used; 114349030 free inodes.

server4 `/home`: 105747968000 available bytes; 94.10% used; 114349030 free inodes.

server4 `/data`: 154569232384 available bytes; 97.86% used; 225273208 free inodes.

server4 `/tmp`: 105747968000 available bytes; 94.10% used; 114349030 free inodes.

server4 `/var/tmp`: 105747968000 available bytes; 94.10% used; 114349030 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
