# V2R cluster inventory

2026-09-27T10:01:53.241457+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314437107712 available bytes; 82.46% used; 112440717 free inodes.

server1 `/home`: 314437107712 available bytes; 82.46% used; 112440717 free inodes.

server1 `/tmp`: 314437107712 available bytes; 82.46% used; 112440717 free inodes.

server1 `/var/tmp`: 314437107712 available bytes; 82.46% used; 112440717 free inodes.

server1 `/mnt/raid5`: 635420565504 available bytes; 97.09% used; 337424412 free inodes.
| server2 | True | ['1', '2', '7'] | [] | reference_compatible=False |

server2 `/`: 16508129280 available bytes; 99.08% used; 110356832 free inodes.

server2 `/home`: 16508129280 available bytes; 99.08% used; 110356832 free inodes.

server2 `/tmp`: 16508129280 available bytes; 99.08% used; 110356832 free inodes.

server2 `/var/tmp`: 16508129280 available bytes; 99.08% used; 110356832 free inodes.

server2 `/mnt/raid5`: 572664115200 available bytes; 96.04% used; 444740562 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78545170432 available bytes; 95.62% used; 114062834 free inodes.

server3 `/home`: 78545170432 available bytes; 95.62% used; 114062834 free inodes.

server3 `/data`: 1332249374720 available bytes; 81.59% used; 225761573 free inodes.

server3 `/tmp`: 78545170432 available bytes; 95.62% used; 114062834 free inodes.

server3 `/var/tmp`: 78545170432 available bytes; 95.62% used; 114062834 free inodes.
| server4 | True | ['0', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111049535488 available bytes; 93.80% used; 114372849 free inodes.

server4 `/home`: 111049535488 available bytes; 93.80% used; 114372849 free inodes.

server4 `/data`: 363948544000 available bytes; 94.97% used; 224767150 free inodes.

server4 `/tmp`: 111049535488 available bytes; 93.80% used; 114372849 free inodes.

server4 `/var/tmp`: 111049535488 available bytes; 93.80% used; 114372849 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
