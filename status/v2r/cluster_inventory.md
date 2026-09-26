# V2R cluster inventory

2026-09-26T06:39:12.413111+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318768291840 available bytes; 82.22% used; 112476272 free inodes.

server1 `/home`: 318768291840 available bytes; 82.22% used; 112476272 free inodes.

server1 `/tmp`: 318768291840 available bytes; 82.22% used; 112476272 free inodes.

server1 `/var/tmp`: 318768291840 available bytes; 82.22% used; 112476272 free inodes.

server1 `/mnt/raid5`: 219346841600 available bytes; 98.99% used; 337539705 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22314221568 available bytes; 98.76% used; 110403837 free inodes.

server2 `/home`: 22314221568 available bytes; 98.76% used; 110403837 free inodes.

server2 `/tmp`: 22314221568 available bytes; 98.76% used; 110403837 free inodes.

server2 `/var/tmp`: 22314221568 available bytes; 98.76% used; 110403837 free inodes.

server2 `/mnt/raid5`: 272760631296 available bytes; 98.12% used; 445028814 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82563784704 available bytes; 95.39% used; 114110888 free inodes.

server3 `/home`: 82563784704 available bytes; 95.39% used; 114110888 free inodes.

server3 `/data`: 123995869184 available bytes; 98.29% used; 225822130 free inodes.

server3 `/tmp`: 82563784704 available bytes; 95.39% used; 114110888 free inodes.

server3 `/var/tmp`: 82563784704 available bytes; 95.39% used; 114110888 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106076012544 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106076012544 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 106035486720 available bytes; 98.53% used; 224923323 free inodes.

server4 `/tmp`: 106076012544 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106076012544 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
