# V2R cluster inventory

2026-09-24T19:03:11.058146+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323995467776 available bytes; 81.93% used; 112481464 free inodes.

server1 `/home`: 323995467776 available bytes; 81.93% used; 112481464 free inodes.

server1 `/tmp`: 323995467776 available bytes; 81.93% used; 112481464 free inodes.

server1 `/var/tmp`: 323995467776 available bytes; 81.93% used; 112481464 free inodes.

server1 `/mnt/raid5`: 416248713216 available bytes; 98.09% used; 337635528 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 54469611520 available bytes; 96.96% used; 110411925 free inodes.

server2 `/home`: 54469611520 available bytes; 96.96% used; 110411925 free inodes.

server2 `/tmp`: 54469611520 available bytes; 96.96% used; 110411925 free inodes.

server2 `/var/tmp`: 54469611520 available bytes; 96.96% used; 110411925 free inodes.

server2 `/mnt/raid5`: 495695687680 available bytes; 96.57% used; 445159613 free inodes.
| server3 | True | ['1'] | [] | reference_compatible=True |

server3 `/`: 84406812672 available bytes; 95.29% used; 114156137 free inodes.

server3 `/home`: 84406812672 available bytes; 95.29% used; 114156137 free inodes.

server3 `/data`: 152514633728 available bytes; 97.89% used; 225799956 free inodes.

server3 `/tmp`: 84406812672 available bytes; 95.29% used; 114156137 free inodes.

server3 `/var/tmp`: 84406812672 available bytes; 95.29% used; 114156137 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105660878848 available bytes; 94.10% used; 114348475 free inodes.

server4 `/home`: 105660878848 available bytes; 94.10% used; 114348475 free inodes.

server4 `/data`: 89911353344 available bytes; 98.76% used; 225267266 free inodes.

server4 `/tmp`: 105660878848 available bytes; 94.10% used; 114348475 free inodes.

server4 `/var/tmp`: 105660878848 available bytes; 94.10% used; 114348475 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
