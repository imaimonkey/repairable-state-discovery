# V2R cluster inventory

2026-09-27T14:47:04.421888+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304749273088 available bytes; 83.00% used; 112401411 free inodes.

server1 `/home`: 304749273088 available bytes; 83.00% used; 112401411 free inodes.

server1 `/tmp`: 304749273088 available bytes; 83.00% used; 112401411 free inodes.

server1 `/var/tmp`: 304749273088 available bytes; 83.00% used; 112401411 free inodes.

server1 `/mnt/raid5`: 630117044224 available bytes; 97.11% used; 337424046 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 13406126080 available bytes; 99.25% used; 110351798 free inodes.

server2 `/home`: 13406126080 available bytes; 99.25% used; 110351798 free inodes.

server2 `/tmp`: 13406126080 available bytes; 99.25% used; 110351798 free inodes.

server2 `/var/tmp`: 13406126080 available bytes; 99.25% used; 110351798 free inodes.

server2 `/mnt/raid5`: 525916200960 available bytes; 96.37% used; 444721988 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78557810688 available bytes; 95.62% used; 114062777 free inodes.

server3 `/home`: 78557810688 available bytes; 95.62% used; 114062777 free inodes.

server3 `/data`: 1328700342272 available bytes; 81.64% used; 225756675 free inodes.

server3 `/tmp`: 78557810688 available bytes; 95.62% used; 114062777 free inodes.

server3 `/var/tmp`: 78557810688 available bytes; 95.62% used; 114062777 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109761630208 available bytes; 93.87% used; 114372745 free inodes.

server4 `/home`: 109761630208 available bytes; 93.87% used; 114372745 free inodes.

server4 `/data`: 350427385856 available bytes; 95.16% used; 224727316 free inodes.

server4 `/tmp`: 109761630208 available bytes; 93.87% used; 114372745 free inodes.

server4 `/var/tmp`: 109761630208 available bytes; 93.87% used; 114372745 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
