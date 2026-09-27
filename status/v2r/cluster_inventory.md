# V2R cluster inventory

2026-09-27T10:21:43.816933+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314441388032 available bytes; 82.46% used; 112440677 free inodes.

server1 `/home`: 314441388032 available bytes; 82.46% used; 112440677 free inodes.

server1 `/tmp`: 314441388032 available bytes; 82.46% used; 112440677 free inodes.

server1 `/var/tmp`: 314441388032 available bytes; 82.46% used; 112440677 free inodes.

server1 `/mnt/raid5`: 635418734592 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16511569920 available bytes; 99.08% used; 110356610 free inodes.

server2 `/home`: 16511569920 available bytes; 99.08% used; 110356610 free inodes.

server2 `/tmp`: 16511569920 available bytes; 99.08% used; 110356610 free inodes.

server2 `/var/tmp`: 16511569920 available bytes; 99.08% used; 110356610 free inodes.

server2 `/mnt/raid5`: 572051353600 available bytes; 96.05% used; 444739944 free inodes.
| server3 | True | ['0', '2'] | [] | reference_compatible=True |

server3 `/`: 78543761408 available bytes; 95.62% used; 114062827 free inodes.

server3 `/home`: 78543761408 available bytes; 95.62% used; 114062827 free inodes.

server3 `/data`: 1332187856896 available bytes; 81.59% used; 225761051 free inodes.

server3 `/tmp`: 78543761408 available bytes; 95.62% used; 114062827 free inodes.

server3 `/var/tmp`: 78543761408 available bytes; 95.62% used; 114062827 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111040532480 available bytes; 93.80% used; 114372828 free inodes.

server4 `/home`: 111040532480 available bytes; 93.80% used; 114372828 free inodes.

server4 `/data`: 363672178688 available bytes; 94.97% used; 224766908 free inodes.

server4 `/tmp`: 111040532480 available bytes; 93.80% used; 114372828 free inodes.

server4 `/var/tmp`: 111040532480 available bytes; 93.80% used; 114372828 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
