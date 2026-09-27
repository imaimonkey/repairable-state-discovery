# V2R cluster inventory

2026-09-27T14:07:23.183175+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748699648 available bytes; 83.00% used; 112401361 free inodes.

server1 `/home`: 304748699648 available bytes; 83.00% used; 112401361 free inodes.

server1 `/tmp`: 304748699648 available bytes; 83.00% used; 112401361 free inodes.

server1 `/var/tmp`: 304748699648 available bytes; 83.00% used; 112401361 free inodes.

server1 `/mnt/raid5`: 632987578368 available bytes; 97.10% used; 337424118 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13407895552 available bytes; 99.25% used; 110351811 free inodes.

server2 `/home`: 13407895552 available bytes; 99.25% used; 110351811 free inodes.

server2 `/tmp`: 13407895552 available bytes; 99.25% used; 110351811 free inodes.

server2 `/var/tmp`: 13407895552 available bytes; 99.25% used; 110351811 free inodes.

server2 `/mnt/raid5`: 527459098624 available bytes; 96.36% used; 444723103 free inodes.
| server3 | True | ['2'] | [] | reference_compatible=True |

server3 `/`: 78559645696 available bytes; 95.62% used; 114062772 free inodes.

server3 `/home`: 78559645696 available bytes; 95.62% used; 114062772 free inodes.

server3 `/data`: 1330661416960 available bytes; 81.61% used; 225757151 free inodes.

server3 `/tmp`: 78559645696 available bytes; 95.62% used; 114062772 free inodes.

server3 `/var/tmp`: 78559645696 available bytes; 95.62% used; 114062772 free inodes.
| server4 | True | ['0', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110996869120 available bytes; 93.81% used; 114372787 free inodes.

server4 `/home`: 110996869120 available bytes; 93.81% used; 114372787 free inodes.

server4 `/data`: 350773542912 available bytes; 95.15% used; 224727429 free inodes.

server4 `/tmp`: 110996869120 available bytes; 93.81% used; 114372787 free inodes.

server4 `/var/tmp`: 110996869120 available bytes; 93.81% used; 114372787 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
