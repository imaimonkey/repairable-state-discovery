# V2R cluster inventory

2026-09-27T09:49:42.314341+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314443472896 available bytes; 82.46% used; 112440743 free inodes.

server1 `/home`: 314443472896 available bytes; 82.46% used; 112440743 free inodes.

server1 `/tmp`: 314443472896 available bytes; 82.46% used; 112440743 free inodes.

server1 `/var/tmp`: 314443472896 available bytes; 82.46% used; 112440743 free inodes.

server1 `/mnt/raid5`: 635438424064 available bytes; 97.09% used; 337424416 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16515235840 available bytes; 99.08% used; 110356909 free inodes.

server2 `/home`: 16515235840 available bytes; 99.08% used; 110356909 free inodes.

server2 `/tmp`: 16515235840 available bytes; 99.08% used; 110356909 free inodes.

server2 `/var/tmp`: 16515235840 available bytes; 99.08% used; 110356909 free inodes.

server2 `/mnt/raid5`: 572543852544 available bytes; 96.04% used; 444741188 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78546812928 available bytes; 95.62% used; 114062908 free inodes.

server3 `/home`: 78546812928 available bytes; 95.62% used; 114062908 free inodes.

server3 `/data`: 1332464852992 available bytes; 81.58% used; 225761976 free inodes.

server3 `/tmp`: 78546812928 available bytes; 95.62% used; 114062908 free inodes.

server3 `/var/tmp`: 78546812928 available bytes; 95.62% used; 114062908 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111049883648 available bytes; 93.80% used; 114372850 free inodes.

server4 `/home`: 111049883648 available bytes; 93.80% used; 114372850 free inodes.

server4 `/data`: 364003770368 available bytes; 94.97% used; 224767147 free inodes.

server4 `/tmp`: 111049883648 available bytes; 93.80% used; 114372850 free inodes.

server4 `/var/tmp`: 111049883648 available bytes; 93.80% used; 114372850 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
