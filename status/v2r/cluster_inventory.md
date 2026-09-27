# V2R cluster inventory

2026-09-27T09:51:13.680387+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314443276288 available bytes; 82.46% used; 112440741 free inodes.

server1 `/home`: 314443276288 available bytes; 82.46% used; 112440741 free inodes.

server1 `/tmp`: 314443276288 available bytes; 82.46% used; 112440741 free inodes.

server1 `/var/tmp`: 314443276288 available bytes; 82.46% used; 112440741 free inodes.

server1 `/mnt/raid5`: 635435556864 available bytes; 97.09% used; 337424414 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16515022848 available bytes; 99.08% used; 110356909 free inodes.

server2 `/home`: 16515022848 available bytes; 99.08% used; 110356909 free inodes.

server2 `/tmp`: 16515022848 available bytes; 99.08% used; 110356909 free inodes.

server2 `/var/tmp`: 16515022848 available bytes; 99.08% used; 110356909 free inodes.

server2 `/mnt/raid5`: 573026091008 available bytes; 96.04% used; 444741012 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78546575360 available bytes; 95.62% used; 114062908 free inodes.

server3 `/home`: 78546575360 available bytes; 95.62% used; 114062908 free inodes.

server3 `/data`: 1332326817792 available bytes; 81.59% used; 225761889 free inodes.

server3 `/tmp`: 78546575360 available bytes; 95.62% used; 114062908 free inodes.

server3 `/var/tmp`: 78546575360 available bytes; 95.62% used; 114062908 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111049826304 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111049826304 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364003733504 available bytes; 94.97% used; 224767147 free inodes.

server4 `/tmp`: 111049826304 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111049826304 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
